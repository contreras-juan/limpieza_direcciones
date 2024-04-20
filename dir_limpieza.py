import pandas as pd
import re
from unidecode import unidecode
import string

def separate_numbers_from_text(input_string):

  '''
    Esta función separa los números de los textos
  '''
  return re.sub(r'(\d+|[A-Z]+)', r' \1 ', input_string)

def separate_word(text):
  '''
    Esta función separa las palabras 'sur' y 'este' de algún número
  '''
  pattern = r'(\d{1}|[a-zA-Z]{1})(este|sur)'
  result = re.sub(pattern, r'\1 \2', text)
  return result
    
def apply_replacements(input_string):


  '''
    Esta función hace reemplazos de algunos errores tipográficos
  '''
  replace_dict = {
      'kr': 'carrera', 
#        'tras': 'transversal',
      'trasv': 'transversal',
      'trans': 'transversal',
      'ak': 'avenida carrera',
      'avenia': 'avenida',
      'krr': 'carrera',
      'cr': 'carrera',
      'carera': 'carrera',
      'cra': 'carrera',
      'km': 'kilometro', 
      'av': 'avenida',
      'cara': 'carrera',
      'tv': 'transversal',
      'kra': 'carrera',
      'diag': 'diagonal',
      'dg': 'diagonal',
      'digonal': 'diagonal',
      'ave': 'avenida',
      'carr': 'carrera',
      'cl': 'calle',
      'cll': 'calle',
      'clle': 'calle',
      'tranv': 'tras',
      'dig': 'diagonal',
      'tranversal': 'transversal',
      'calloe': 'calle',
      'crrera': 'carrera',
      'crr': 'carrera',
      'ac': 'avenida calle',
      'diaginal': 'diagonal',
      'calke': 'calle',
      'trv': 'transversal',
      'transvelsal': 'transversal',
      'karerra': 'carrera',
      'call': 'calle',
      'avda': 'avenida',
      'carrerac': 'carrera',
      'carrea': 'carrera',
      'trav': 'transversal',
      'carre': 'carrera',
      'cakle': 'calle',
      'dagonal': 'diagonal',
      'traversal': 'transversal',
      'cakke': 'calle',
#        'c': 'calle',
      '1cll': 'calle',
      'cal': 'calle',
      'tranvs': 'transversal',
      'callee': 'calle',
      'cale': 'calle',
      'trasversal': 'transversal',
      'cacalle': 'calle',
      'carrrera': 'carrera',
      'transv': 'transversal',
      'crra': 'carrera',
      'car': 'carrera',
      'karrera': 'carrera',
      'celle': 'calle',
      'carreta': 'carrera',
      'carreara': 'carrera',
      'carrara': 'carrera', 
      'carrerab': 'carrera',
      'trasnversal': 'transversal', 
      'transversak': 'transversal',
      'csrrera': 'carrera',
      'carra': 'carrera',
      'calee': 'calle',
      'canle': 'calle',
      'avcarrera': 'avenida carrera',
      'cella': 'calle',
      'carrwra': 'carrera',
      'carerra': 'carrera',
      'diganal': 'diagonal',
      'avenilla': 'avenida',
      'calla': 'calle',
      'clla': 'calle',
      'avcl': 'avenida calle',
      'carrer': 'carrera',
      'clll': 'calle',
      'traversar': 'transversal',
      'trasvesar': 'transversal',
      'akra': 'avenida carrera',
      'transversl': 'transversal', 
      'tranvwrsal': 'transversal',
      'krra': 'carrera',
      'avcalle': 'avenida calle',
      'carreras': 'carrera',
      'travs': 'transversal',
      'avcr': 'avenida carrera',
      'alle': 'calle',
      'karera': 'carrera', 
      'callle': 'calle',
      'carrere': 'carrera', 
      'catrera': 'carrera',
      'callev': 'calle',
      'called': 'calle',
      'cartera': 'carrera',
      'transveral': 'transversal',
      '\tcra': 'carrera',
      'kilometre': 'kilometro',
      'trabversal': 'transversal',
      'cle': 'calle',
      'diagonsl': 'diagonal',
      'avk': 'avenida carrera',
      'clk': 'calle',
      'calld': 'calle',
      'calne': 'calle',
#        'k': 'carrera',
      'tr': 'transversal',
      'trvl': 'transversal',
      'callo': 'calle',
      'no': '',
      'con': '',
      'numero': '',
      'k r': 'carrera',
      'nro': '',
      'no.': '',
      'deg': '',
      'ndeg': ''
  }

#    keys = replace_dict.keys()

#    for j in keys:
#        value = replace_dict[j]
#        result = re.sub(j, '', input_string)

  pattern = r'\b(?:' + '|'.join(re.escape(key) for key in replace_dict.keys()) + r')\b'
  regex = re.compile(pattern)
  result = regex.sub(lambda match: replace_dict[match.group(0)], input_string)

  replace_dict2 = {
      'avenida cali': 'avenida carrera 86',
      'avenida boyaca': 'avenida carrera 72',
      'avenida caracas': 'carrera 14'    
      }

  pattern = r'\b(?:' + '|'.join(re.escape(key) for key in replace_dict2.keys()) + r')\b'
  regex = re.compile(pattern)
  result = regex.sub(lambda match: replace_dict2[match.group(0)], result)
  
  return result
    
def str_limpieza(dir: str):

  '''
    Esta función estandariza las direcciones
  '''

  dir = str(dir)
  dir = unidecode(dir)

  dir = dir.lower()

  dir = dir.strip()
  
  for substr in string.punctuation + '°':
      dir = dir.replace(substr, ' ')
      dir = dir.replace(substr, '')

  for substr in ['torre', 'apto', 'int', 'interior', 'appartamento', 'conjunto', 
                  'esquina', 'eskina', 'barrio', 'piso', 'casa', 'ap', 'in', 'manzana',
                  'brr', 'bogota', 'local', 'bloque', 'primer', 'segundo', 'tercero', 'cuarto',
                  'frente', 'consultorio', 'edificio']:


      dir = re.sub(f' {substr}.*$', '', dir)

  dir = separate_numbers_from_text(dir)

  dir = separate_word(dir)

  dir = unidecode(dir)

  dir = apply_replacements(dir)

  pattern = r'0+(\d)\b'
  dir = re.sub(pattern, r'\1', dir)

  pattern = r'(?<!avenida )(?<!^)(\bcalle\b|\bcarrera\b)'
  dir = re.sub(pattern, '', dir)

  dir = re.sub(r'\s{2,}', ' ', dir)

  pattern = r'(\w)(bis)'
  dir = re.sub(pattern, r'\1 \2', dir)
  
  dir = dir.strip()
  
  return dir