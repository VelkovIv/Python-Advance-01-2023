from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InaVidCharactersError(Exception):
    pass


email_name_regex = r'([a-z1-9\._]+)'  # regex for email names validations
domain_name_regex = r'(\.[a-z]+)$'  # regex for domain names validations
MIN_NAME_LENGTH = 4

valid_domains = [".com", ".bg", ".org", ".net"]

email = input()

while email != "End":
    try:
        if len(email.split("@")[0]) <= MIN_NAME_LENGTH:
            raise NameTooShortError("Name must be more than 4 characters")

        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @ symbol")

        if findall(domain_name_regex, email)[0] not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        if findall(email_name_regex, email)[0] != email.split("@")[0]:
            raise InaVidCharactersError("Email must contain only lower case letters, numbers, underscores and dots")

    except IndexError:  # invalid input is return as error if not of above check works but there no valid email entered
        print("Invalid email!")

    else:
        print("Email is valid")

    email = input()