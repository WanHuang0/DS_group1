#!/bin/bash
set -e

wandb login --relogin $WANDB_TOKEN

exec "$@"


