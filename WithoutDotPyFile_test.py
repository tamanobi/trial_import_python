import importlib.util
import importlib.machinery

# see https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_loader
loader = importlib.machinery.SourceFileLoader(
    'wdpf', 'WithoutDotPyFile')
spec = importlib.util.spec_from_loader(loader.name, loader)
wdpf = importlib.util.module_from_spec(spec)
loader.exec_module(wdpf)

wdpf.hello()
