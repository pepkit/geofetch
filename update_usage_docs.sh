# Run this script to build and deploy the mkdocs docs in /docs

JUPYTER_SOURCE=""
JUPYTER_BUILD=""
AUTODOC_MODULES=()
AUTODOC_BUILD=""
USAGE_TEMPLATE="docs/usage_template.md"
USAGE_CMDS=("geofetch --help")


# Build an auto-usage page in markdown
if [ ! -z "$USAGE_CMDS" ]
then
  cp $USAGE_TEMPLATE usage_template.md
  for cmd in "$USAGE_CMDS"; do
    echo $cmd
    echo -e "\n\`$cmd\`" >> usage_template.md
    echo -e '```{console}' >> usage_template.md
    $cmd >> usage_template.md 2>&1
    echo -e '```' >> usage_template.md
  done
  mv usage_template.md  docs/usage.md
  cat docs/usage.md
else
  echo "No USAGE_CMDS provided."
fi

