class Cryptographer:
    class CryptographyError (Exception):
        def __init__(self, method="Unspecified", error="Unspecified"):
            super ().__init__ (f"Error raised by {method}: {error}")

    @staticmethod
    def c_shift_word(key, _in, reverse=False):
        try:
            rev = [1, -1][reverse]
            return "".join (
                [chr (ord (i[0]) + rev * ord (key[i[1] % len (key)])) for i in zip (_in, range (len (_in)))])
        except ValueError:
            raise Cryptographer.CryptographyError (method="c_shift_word",
                                                   error="Invalid reverse value or input")