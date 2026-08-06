import argparse
import os

def minify_js(source: str) -> str:
    """Minify JavaScript code by removing comments and unnecessary whitespace."""
    out = []
    i = 0
    n = len(source)
    state = "normal"
    delim = ""

    while i < n:
        c = source[i]
        nc = source[i + 1] if i + 1 < n else ""

        if state == "normal":
            if c == "/" and nc == "/":
                i += 2
                while i < n and source[i] not in "\r\n":
                    i += 1
                continue
            if c == "/" and nc == "*":
                i += 2
                while i < n - 1 and not (source[i] == "*" and source[i + 1] == "/"):
                    i += 1
                i += 2
                continue
            if c in ('"', "'"):
                delim = c
                state = "string"
                out.append(c)
                i += 1
                continue
            if c == "`":
                state = "template"
                out.append(c)
                i += 1
                continue
            if c.isspace():
                j = i + 1
                while j < n and source[j].isspace():
                    j += 1
                if out:
                    prev = out[-1]
                    next_char = source[j] if j < n else ""
                    if (
                        prev not in " "
                        and prev not in "([{,;:+-*/%&|^!~=<>?"
                        and next_char not in " \")]}},;:+-*/%&|^!~=<>?"
                        and next_char != ""
                    ):
                        out.append(" ")
                i = j
                continue
            out.append(c)
            i += 1
            continue

        if state == "string":
            out.append(c)
            if c == "\\":
                if i + 1 < n:
                    out.append(source[i + 1])
                    i += 2
                    continue
            if c == delim:
                state = "normal"
            i += 1
            continue

        if state == "template":
            out.append(c)
            if c == "\\":
                if i + 1 < n:
                    out.append(source[i + 1])
                    i += 2
                    continue
            if c == "`":
                state = "normal"
                i += 1
                continue
            if c == "$" and nc == "{":
                out.append(nc)
                i += 2
                continue
            i += 1
            continue

    return "".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Minify a JavaScript file.")
    parser.add_argument("source", help="Path to the input JavaScript file.")
    parser.add_argument("-o", "--output", help="Path to the minified output file.")
    args = parser.parse_args()

    if not os.path.isfile(args.source):
        raise FileNotFoundError(f"Source file not found: {args.source}")

    with open(args.source, "r", encoding="utf-8") as infile:
        source_code = infile.read()

    minified = minify_js(source_code)

    output_path = args.output or f"{os.path.splitext(args.source)[0]}.min.js"
    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(minified)

    print(f"Minified {args.source} -> {output_path}")


if __name__ == "__main__":
    main()
