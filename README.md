# BibTeXManager

`BibTeXManager` is a Python utility designed to automate the enhancement of BibTeX files by fetching and adding missing Digital Object Identifiers (DOIs) to bibliography entries. This tool is especially useful for academic and scientific writing where referencing DOI-enabled citations is necessary for the reproducibility and accessibility of cited resources.

## Features

- **DOI Fetching**: Automatically fetches DOIs for BibTeX entries using the Crossref API.
- **DOI Formatting**: Ensures DOIs are formatted as clickable URLs.

## Prerequisites

Before you start using `BibTeXManager`, make sure you have Python installed on your system. Python 3.6 or above is recommended. You also need to install the `requests` and `bibtexparser` libraries, which can be installed via pip:

```bash
python -m pip install -r requirements.txt
```

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/ClaireGyn/BibTeXManager.git
cd BibTeXManager
```

## Usage

Run the script by executing the following command in your terminal.

```bash
python bibtex_manager.py <input_file.bib> <output_file.bib>
```

You need to specify the paths to your input and output files to execute the script:

1. **Input Path**: **the absolute path** of your old `.bib` file. This is the file that you want to update.

2. **Output Path**: **the absolute path** for the output `.bib` file where the updated version will be saved.

The command will process the specified BibTeX file, fetch missing DOIs, and save the updated entries to the output file.

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
