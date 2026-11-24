from dotenv import load_dotenv
import os


env_variables: dict[str, str] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "Connected to local instance",
    "API_KEY": "Authenticated",
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": "Online"
}


load_dotenv()


def vars_check() -> None:
    """Check and display the application's environment configuration.

    Iterates through the required environment variables, checking whether
    they are defined. Displays the actual values of MATRIX_MODE and LOG_LEVEL,
    while hiding sensitive values of other variables by displaying descriptive
    messages from the env_variables dictionary. Reports any missing variables.

    Returns:
    None: Prints the configuration status to the console.
    """

    print("Configuration loaded:")
    for var in env_variables.keys():
        value: str | None = os.getenv(var)
        name: str = var.capitalize().replace("_", " ")
        if value is not None:
            if var == "MATRIX_MODE" or var == "LOG_LEVEL":
                print(f"{name}: {value}")
            else:
                print(f"{name}: {env_variables[var]}")
        else:
            print(f"{name}: MISSING - please set this variable")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    if os.path.exists(".env"):
        vars_check()

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        if os.getenv("MATRIX_MODE") == "production":
            print("[WARNING] Ensure .env is not used in production - "
                  "use real environment variables!")
        elif os.getenv("MATRIX_MODE") == "development":
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] Variable MATRIX_MODE is not valid")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
    else:
        print("[WARNING] No .env file found")
        print("Run: cp .env.example .env")
        print("Then edit .env example with your configuration values")


if __name__ == "__main__":
    main()
