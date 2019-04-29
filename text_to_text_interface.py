import os
import argparse

MODEL_DIR = './wmt14.en-fr.fconv-py'

# Translation interface
def translate_page(input_string, src_lang, target_lang):
  if not os.path.exists(MODEL_DIR):
    print('ERROR: Model must be downloaded and added to the working path')

  try:
    os.system("echo {} | fairseq-interactive --path {}/model.pt {} --beam 5 --source-lang en --target-lang fr --cpu > out.txt 2> err.txt".format(input_string, MODEL_DIR, MODEL_DIR))
  except Exception as e:
    print(e)
    print('ERROR: Language not supported')

  with open('out.txt', 'r') as f:
    out = f.readlines()
    print(len(out))
    out = out[-2].split('\t')
    # TODO: Handle worst case of sentence having tabs
    # Remove @, (, ) and double spaces
    translation = " ".join(out[2].replace('@', '').replace('(', '').replace(')', '').split())
    return translation


def main():
  parser = argparse.ArgumentParser(description='PyTorch Language Translation API')
  parser.add_argument('--input_sentence', type=str, default='None', metavar='N',
                      help='input sentence to translate')
  args = parser.parse_args()
  input = args.input_sentence
  out = translate_page(input, 'en', 'fr')
  print('Translation: ', out)

if __name__ == '__main__':
  main()
