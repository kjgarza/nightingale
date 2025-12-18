import click
import csv
from nightingale import nightingale


@click.command()
@click.argument('input', type=str)
@click.option('-o', '--output', type=str, help='Output file for prioritized issues')
@click.option('-v', '--verbose', is_flag=True, help='Print verbose output')
def main(input, output, verbose):
    """Nightingale - GitHub Issues Prioritizer
    
    Prioritize GitHub issues using interactive comparisons.
    
    INPUT: CSV file with GitHub issues names and links or URL to GitHub repo issue list
    
    \b
    Examples:
        nightingale issues.csv
        nightingale https://example.com/issues.csv
        nightingale issues.csv -o prioritized.csv
        nightingale issues.csv -v
    
    \b
    How it works:
        The tool will present you with pairs of issues and ask you to choose
        which one is more important. Based on your choices, it will build a
        prioritized list using a binary insert sort algorithm.
    
        For each comparison, enter:
        - '1' to select the first issue as more important
        - '2' to select the second issue as more important
    """
    if verbose:
        click.echo(f"Processing issues from: {input}")
        if output:
            click.echo(f"Output will be saved to: {output}")
    
    try:
        issues = nightingale.nightingale(input)
        
        if output:
            # Save to file if output is specified
            with open(output, 'w', newline='') as f:
                writer = csv.writer(f)
                for issue in issues:
                    writer.writerow([issue])
            if verbose:
                click.echo(f"Prioritized issues saved to: {output}")
        elif verbose:
            click.echo("Prioritization complete!")
    except FileNotFoundError as e:
        click.echo(f"Error: File not found - {input}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


if __name__ == "__main__":
    main()