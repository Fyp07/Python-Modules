from importlib.metadata import version, metadata, PackageNotFoundError


packages: list[str] = ["pandas",
                       "numpy",
                       "matplotlib",
                       "vasco"]


def check_dependencies(packages: list[str]) -> bool:
    """Check whether all specified packages are installed.

    Args:
    packages (list[str]): A list of package names to check.

    Returns:
    bool: True if all packages are installed, False otherwise.
    """

    is_available = True
    for package in packages:
        try:
            version(package)
        except PackageNotFoundError:
            is_available = False
            print(f"{package} is missing.")
    return is_available


def display_packages(packages: list[str]) -> None:
    """Display information about the installed packages.

    Args:
    packages (list[str]): A list of package names to check and display.

    Returns:
    None: Prints each package's name, version,
    and summary if all dependencies are installed.
    """

    print("Checking dependencies:")
    if check_dependencies(packages):
        for package in packages:
            print(
                f"[OK] {package} ({version(package)})"
                f" - {metadata(package)['Summary']}"
            )


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if check_dependencies(packages):
        display_packages(packages)
        import numpy
        import pandas
        import matplotlib.pyplot as mat

        print("\nAnalyzing Matrix Data...")
        data = numpy.random.randn(250, 6)
        columns: list[str] = ["Neuza", "Gabriel", "Davi",
                              "Maria Paula", "Danielle", "Felyppe"]
        print(f"Processing {data.size} data points...")
        data_frame = pandas.DataFrame(data=data, columns=columns)
        de_sum = data_frame.cumsum()
        print("Generating Visualization..")
        mat.figure(figsize=(10, 6), facecolor="#F2E9D8")
        mat.plot(de_sum["Neuza"], label="Neuza", color="#7754F5")
        mat.plot(de_sum["Gabriel"], label="Gabriel", color="#F2C335")
        mat.plot(de_sum["Maria Paula"], label="Maria Paula", color="#FF4885")
        mat.plot(de_sum["Danielle"], label="Danielle", color="#02730F")
        mat.plot(de_sum["Felyppe"], label="Felyppe", color="#1B11F0")
        mat.plot(de_sum["Davi"], label="Davi", color="#FF8800")
        mat.title("Matrix data", fontsize=16)
        mat.grid(True, linestyle="dashdot", alpha=0.6)
        mat.legend()
        mat.savefig("matrix_analysis.png", dpi=100)
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    else:
        print("\nTo install missing dependencies use:")
        print("For pip:")
        print(" 'pip install -r requirements.txt'")
        print("For Poetry:")
        print(" 'poetry install'")
        print(" 'poetry run python loading.py'")


if __name__ == "__main__":
    main()
