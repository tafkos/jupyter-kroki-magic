# Jupyter Kroki Magic

A Jupyter Notebook %%magic for drawing diagrams using kroki.io

Usage
------

Load extension inside a Jupyter notebook:

```
%load_ext krokimagic
```

Add code with Cell magic:

```
%%kroki [diagram-type] [http://alternate.kroki.url:port]

# diagram syntax
```


Examples
--------

```
%%kroki plantuml

skinparam monochrome true
skinparam ranksep 20
skinparam dpi 150
skinparam arrowThickness 0.7
skinparam packageTitleAlignment left
skinparam usecaseBorderThickness 0.4
skinparam defaultFontSize 12
skinparam rectangleBorderThickness 1

rectangle "Main" {
  (main.view)
  (singleton)
}
rectangle "Base" {
  (base.component)
  (component)
  (model)
}
rectangle "<b>main.ts</b>" as main_ts

(component) ..> (base.component)
main_ts ==> (main.view)
(main.view) --> (component)
(main.view) ...> (singleton)
(singleton) ---> (model)
```

Installation
------------

    $ pip install jupyter-kroki-magic
