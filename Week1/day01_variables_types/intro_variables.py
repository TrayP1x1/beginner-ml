def describe_value(name: str, value: object) -> None:
    print(f"{name} = {value!r} (type: {type(value).__name__})")


def main() -> None:
    learner_name = "Tray"
    learner_age = 23
    wants_the_job = True
    study_hours_today = 1.5
    number_text = "42"

    converted_to_int = int(number_text)
    converted_to_float = float(number_text)

    describe_value("learner_name", learner_name)
    describe_value("learner_age", learner_age)
    describe_value("wants_the_job", wants_the_job)
    describe_value("study_hours_today", study_hours_today)
    describe_value("number_text", number_text)
    describe_value("converted_to_int", converted_to_int)
    describe_value("converted_to_float", converted_to_float)

    print()
    print("Use int for whole numbers.")
    print("Use float for decimal values.")
    print("Use str for text data.")


if __name__ == "__main__":
    main()
