import string

class DataClean:
    def __init__(self):
        pass
    def _validate_ascii(self, data_string):
        if data_string in string.ascii_lowercase or string.ascii_uppercase:
            return True
        else:
            return False

    def _validate_email(self, email_address):

        #Set counter
        counter = 0

        # Set Check point, that check certain objective is achieved
        # by decreasing value by 1
        # 0 email is valid
        # 1 there is no @ symbol
        # 2 there is no .(dot) domain symbol
        check_point = 2

        # Iterates email address string
        for counter in range(len(email_address)):
            # Check whether @ symbol is found
            if email_address[counter] == '@':
                # If @ is found, then counter2 is set by adding 1 to skip @.
                counter2 = counter + 1
                check_point = check_point - 1

                # Iterates only character after @ symbol
                for x in range(counter2, len(email_address)):
                    # Check whether the chars have .(dot) to validate domain
                    if email_address[x] == '.':
                        pass
                        check_point = check_point - 1

        # If email is valid the function return 0
        return check_point
