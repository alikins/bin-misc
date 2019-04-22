#!/bin/bash

# Will create a bash alias for each venv found in
# ${VENV_DIR} (~/venvs by default).
#
# The aliases will be of form 'venv_$NAME_OF_VENV', ie
# ~/venvs/django22_py36 will have an alias like
# venv_django22_py36.
#
# The alias is just a shortcut to source'ing the 'activate' shell
#
# 'source'ed it directly
#
#  source ~/bin/venv_create_aliases.sh

VENV_DIR=${VENV_DIR:-~/venvs}

# pushd "${VENV_DIR}"
STARTDIR=$(pwd)

cd "${VENV_DIR}" || exit

for venv in *;
do
    echo "${venv} creating alias venv_${venv}=source ${VENV_DIR}/${venv}/bin/activate"
    alias "venv_${venv}"="source ${VENV_DIR}/${venv}/bin/activate"
done

cd "${STARTDIR}" || exit
