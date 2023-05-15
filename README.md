# Nightingale - Bug prioritizer

This package utilizes binary insert sort to prioritize bugs from GitHub issues. The goal is to facilitate the task of issue tracking and bug fixing by bringing the most important issues to the forefront.


![](https://raw.githubusercontent.com/kjgarza/nightingale/master/nigthtingale_logo.png)

## Prerequisites

To use this tool, you should have Python installed on your machine. This tool is compatible with Python 3.6 and above.


## Usage

1. Generate a list of bugs from GitHub into a CSV file named `issues.csv`. This CSV file should contain the names and links of the issues.

2. Run the command-line interface (CLI) tool using the `python -m nightingale.cli` command followed by the appropriate arguments.


Arguments:
- `<input>`: The path to the CSV file with GitHub issues names and links or URL to GitHub repo issue list.
- `-o, --output <output>`: (Optional) The path to the output file where the prioritized issues will be stored. If not specified, the output will be printed to the console.
- `-v, --verbose`: (Optional) Enable verbose output.


```shell

python -m nightingale.cli issues.csv

Which issue is more important?
1. 782  `relatedItems` is erroring when `publicationYear` is not supplied       bug     about 18 days ago
2. 764  REST API does not return optional affiliation properties        bug     about 1 month ago
Enter 1 or 2:

```

3. Answer each prompt that appears with the most importan issue. These prompts will guide the tool in prioritizing the issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

