import json


def has_nested_dict(d):
    for v in d.values():
        if isinstance(v, dict):
            return True
    return False


def dict_to_tfvars(py_dict, indent=0, innermost=False):
    tfvars_str = ""

    for key, value in py_dict.items():
        if isinstance(value, dict):
            lf = "\n" if not innermost else ""
            tfvars_str += f"{' ' * indent}{key} = {{{lf}"
            tfvars_str += dict_to_tfvars(
                value, indent + 2, innermost=not has_nested_dict(value)
            )
            tfvars_str += f"{' ' * indent}}}\n"
        else:
            # Convert the value to HCL2 syntax based on its type
            if isinstance(value, str):
                hcl_value = f'"{value}"'
            elif isinstance(value, bool):
                hcl_value = str(value).lower()
            elif isinstance(value, list):
                if len(value) < 2:
                    hcl_value = json.dumps(value)
                else:
                    hcl_value = json.dumps(value, indent=indent + 2).replace(
                        "]", " " * indent + "]"
                    )
            else:
                hcl_value = str(value)

            if innermost:
                key = f'"{key}"'
            tfvars_str += f'{" " * indent}{key} = {hcl_value}\n'

    return tfvars_str


def tfvars_to_file(file, tfvars):
    with open(file, "w") as f:
        f.write(tfvars)


def json_to_dict(file):
    with open(file, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("input", help="input file")
    parser.add_argument("output", help="output file")
    args = parser.parse_args()

    data = json_to_dict(args.input)
    tfvars = dict_to_tfvars(data)
    tfvars_to_file(args.output, tfvars)
