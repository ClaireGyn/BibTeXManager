#!/usr/bin/env python3
"""
BibTeXManager.py

Author: Yaonan Gu
Date: May 6th, 2024
Version: 1.0

Description:
    BibTeXManager is a Python utility designed to enhance BibTeX files by adding missing
    Digital Object Identifiers (DOIs) to the bibliography entries. It fetches DOIs using the
    Crossref API and formats them as clickable URLs.

Copyright:
    Copyright (c) 2024, Yaonan Gu
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
    
    - Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    
    - Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
"""


import requests
import bibtexparser
from requests.exceptions import ChunkedEncodingError, RequestException, Timeout
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

class BibTeXManager:
    def __init__(self, bib_file, output_file):
        self.bib_file = bib_file
        self.output_file = output_file
        self.base_url = "https://api.crossref.org/works"
        self.initial_timeout = 10  # Initial timeout in seconds

    def format_doi(self, doi):
        """Ensure the DOI is formatted as a full URL."""
        prefix = "https://doi.org/"
        if doi.startswith(prefix):
            return doi
        else:
            return prefix + doi

    def fetch_doi(self, title, author, max_attempts=3):
        """Fetch DOI using Crossref API based on title and author with retries."""
        query_params = {'query.title': title, 'query.author': author}
        timeout = self.initial_timeout
        for attempt in range(max_attempts):
            try:
                response = requests.get(self.base_url, params=query_params, timeout=timeout)
                response.raise_for_status()  # Raises HTTPError for bad responses
                results = response.json()
                items = results['message']['items']
                if items:
                    doi = items[0].get('DOI')
                    return self.format_doi(doi)
            except Timeout:
                print(f"Timeout occurred, attempt {attempt + 1} of {max_attempts}, increasing timeout...")
                timeout += 5  # Increase timeout by 5 seconds with each attempt
            except (ChunkedEncodingError, RequestException) as e:
                print(f"Attempt {attempt + 1} of {max_attempts} failed: {e}")
                if attempt == max_attempts - 1:
                    raise
            except Exception as e:
                print(f"An error occurred: {e}")
                break
        return None

    def update_bibtex_doi(self):
        """Update the BibTeX file with DOIs."""
        with open(self.bib_file, 'r') as bibtex_file:
            parser = BibTexParser(common_strings=True)
            parser.customization = convert_to_unicode
            bib_database = bibtexparser.load(bibtex_file)

        for entry in bib_database.entries:
            if 'doi' not in entry:
                doi = self.fetch_doi(entry.get('title', ''), entry.get('author', '').split(',')[0])
                if doi:
                    entry['doi'] = doi
                    print(f"Added DOI for {entry['title']}: {doi}")

        with open(self.output_file, 'w') as bibtex_file:
            bibtexparser.dump(bib_database, bibtex_file)
        print("DOI update completed for BibTeX file.")

# Test
if __name__ == "__main__":
    input_path = input("Please enter the absolute path of your old .bib file: ")
    output_path = input("Please enter the absolute path for the output updated .bib file: ")
    manager = BibTeXManager(input_path, output_path)
    manager.update_bibtex_doi()
