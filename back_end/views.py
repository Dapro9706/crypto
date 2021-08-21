from django.http import JsonResponse
from .crypto import Cryptographer


def crypto(request):
    """

    {
        "input":<str>,
        "key":<str>,
        "reverse":<bool>
    }
    """

    _in = request.GET['input']
    key = request.GET['key']
    rev = int(request.GET['reverse'])
    try:
        out = {"output": Cryptographer.c_shift_word (key, _in, reverse=rev)}
    except Cryptographer.CryptographyError as e:
        out = {'output': f"Error:{e}"}
    return JsonResponse (out)
