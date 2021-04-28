from argparse import Namespace
from clear_lambda_storage import remove_old_lambda_versions, calculate_all_lambdas_size


def clear_lambda_storage(event, context):
    remove_old_lambda_versions(Namespace(token_key_id=None, token_secret=None, regions=None, profile=None))
    return "Successful clean! 🗑 ✅"


def calculate_total_lambda_size(event, context):
    calculate_all_lambdas_size(Namespace(token_key_id=None, token_secret=None, regions=None, profile=None))
    return "Successful count! 🗑 ✅"
