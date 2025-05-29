import importlib.util
import sys

# Caminho para o arquivo .pyc compilado
pyc_path = '__pycache__/siadv2.cpython-313.pyc'

# Carrega o módulo a partir do arquivo .pyc
spec = importlib.util.spec_from_file_location("siadv2", pyc_path)
siadv2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(siadv2)

# Agora, você pode rodar a função main() do siadv2
if __name__ == "__main__":
    siadv2.main()
