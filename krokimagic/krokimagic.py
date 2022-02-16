import requests
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import SVG, display

# see https://kroki.io/examples.html#wbs for working examples

@magics_class
class KrokiMagic(Magics):
    diagrams_supported = set(['blockdiag', 'seqdiag', 'mermaid', 'actdiag', 'nwdiag',
                              'packetdiag', 'rackdiag', 'erd', 'nomnoml', 'plantuml',
                              'umlet', 'wavedrom', 'bpmn', 'bytefield', 'pikchr',
                              'graphviz', 'vega', 'vega-lite', 'ditaa', 'svgbob'])


    def kroki(self, line, cell):
        "simple wrapper for kroki.io"

        splt_line = line.split(sep=' ')

        if splt_line[0] not in self.diagrams_supported:
            raise NotImplemented

        url = 'https://kroki.io'
        if len(splt_line) > 1:
            url = splt_line[1]

        r = requests.post(f'{url}/{splt_line[0]}/svg', json={'diagram_source': cell})
        if r.status_code == 200:
            return display(SVG(r.text))
        else:
            raise ValueError
            
