# random-movie-credits

Creates a realistic continuous movie credit sequence with random content.

Example of what this script does: https://gfycat.com/querulousmajoribis

## How to

run `python3 credits.py`

## Usage

The program comes with lists of names and roles included, but these can be changed to fit your needs. The main rule for these file is one name/role per line.

roles.txt has additional rules since multiple types of roles are tracked in that file.

**#prefix** gives the prefixes used in the roles, i.e. the "Assistant" part of "Assistant Director".

**#crew** is the roles within the crew, i.e. "Director", or "Cinematographer. These do not include actors.

**#actors** include the roles filled by the actors. Some actors will also get given character names randomly generated from the names-files.
