#! python3

# Generates the Invent with Python site from the jinja2 templates.

import os
import logging
import shelve
import distutils.dir_util
import jinja2

GENERATE_ALL = False # If True, all templates are generated regardless if timestamp says they are up to date
BASE_HREF = 'http://localhost:8000/'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Started.')

timestampsShelf = shelve.open('.templateTimestamps')

env = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates', 'content']))

renderCount = 0

# Render all the templates and place them in the output folder
for dirpath, dirnames, filenames in os.walk('content'):
    for filename in filenames:
        if not filename.endswith('.html'):
            continue # skip non-template files

        templateFilename = os.path.join(dirpath, filename)
        if not GENERATE_ALL and (templateFilename in timestampsShelf and timestampsShelf[templateFilename] >= os.path.getmtime(templateFilename)):
            logging.debug('%s is up to date. Skipping.' % (templateFilename))
            continue # not new. skip it

        timestampsShelf[templateFilename] = os.path.getmtime(templateFilename)

        outputFilename = os.path.join('output', dirpath[len('content'):], filename)
        logging.debug('Rendering and writing %s...' % (outputFilename))

        # Render the template
        t = env.get_template(filename)

        # Write the template to the output folder
        outputFo = open(outputFilename, 'w')
        outputFo.write(t.render(base_href=BASE_HREF))
        outputFo.close()

        renderCount += 1

logging.debug('%s templates rendered.' % (renderCount))

# Copy the static folder to the output folder
logging.debug('Copying static files...')
distutils.dir_util.copy_tree('static', 'output', update=True)

logging.debug('Done.')