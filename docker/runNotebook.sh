#!/usr/bin/env bash

root --notebook >& /dev/null #Without --allow-root so that it doesn't start a server

cp /cmpp/docker/jupyter_notebook_config.py /root/.rootnb/jupyter_notebook_config.py

root --notebook
