import requests
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import SVG, display

# see https://kroki.io/examples.html#wbs for working examples

@magics_class
class KrokiMagic(Magics):
    diagrams_supported = set([
        'actdiag', 'blockdiag', 'bpmn', 'bytefield', 'c4plantuml', 'ditaa',
        'erd', 'excalidraw', 'graphviz', 'mermaid', 'nomnoml', 'nwdiag',
        'packetdiag', 'pikchr', 'plantuml', 'rackdiag', 'seqdiag',
        'structurizr', 'svgbob', 'umlet', 'vega', 'vegalite', 'wavedrom'
    ])

    @cell_magic
    def kroki(self, line, cell):
        "simple wrapper for https://kroki.io"

        if line.split(sep=' ')[0] not in self.diagrams_supported:
            raise NotImplemented

        if len(line.split(sep=' ')) <= 1:
            url = 'https://kroki.io'
        else:
            url = line.split(sep=' ')[1]

        r = requests.post(f'{url}/{line.split(sep=" ")[0]}/svg',
                          json={'diagram_source': cell})
        if r.status_code == 200:
            return display(SVG(r.text))
        else:
            raise ValueError
