# BibTeXManager

`BibTeXManager` is a Python utility designed to automate the enhancement of BibTeX files by fetching and adding missing Digital Object Identifiers (DOIs) to bibliography entries. This tool is especially useful for academic and scientific writing where referencing DOI-enabled citations is necessary for the reproducibility and accessibility of cited resources.

## Features

- **DOI Fetching**: Automatically fetches DOIs for BibTeX entries using the Crossref API.
- **DOI Formatting**: Ensures DOIs are formatted as clickable URLs.

## Prerequisites

Before you start using `BibTeXManager`, make sure you have Python installed on your system. Python 3.6 or above is recommended. You also need to install the `requests` and `bibtexparser` libraries, which can be installed via pip:

```bash
pip install requests bibtexparser
```

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/ClaireGyn/BibTeXManager.git
cd BibTeXManager
```

## Usage

To use the `BibTeXManager`, you need to have a `.bib` file ready with entries that potentially lack DOIs. You then run the script by specifying the path to your BibTeX file and the output file name.

### Example Command

```bash
python bibtex_manager.py
```

This command will process the specified BibTeX file, fetch missing DOIs, and save the updated entries to the output file.

### Script Configuration

Modify the `BibTeXManager` class instantiation in the script to point to your specific `.bib` files:

```python
if __name__ == "__main__":
    manager = BibTeXManager('path_to_your_old_bib_file.bib', 'path_to_output_updated_bib_file.bib')
    manager.update_bibtex_doi()
```

Replace `path_to_your_old_bib_file.bib` and `path_to_output_updated_bib_file.bib` with your file paths.

## Contributing

Contributions to `BibTeXManager` are welcome! Here are a few ways you can help:

- Report bugs and issues.
- Suggest new features or improvements.
- Spread the word about `BibTeXManager`.

Please fork the repository and submit pull requests for your proposed changes.

## License

`BibTeXManager` is released under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions or support, please contact [yaonangu@u.nus.edu](mailto:your-email@example.com).
