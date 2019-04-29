import json
import os
import argparse
import subprocess

MODEL_DIR = './wmt14.en-fr.fconv-py'

# Translation interface
def translate_page(input_string, src_lang, dest_lang):
  os.system("echo {} | fairseq-interactive  --path {}/model.pt {}  --beam 5 --source-lang en --target-lang fr > out.txt 2> err.txt".format(input_string, MODEL_DIR, MODEL_DIR))
  with open('out.txt', 'r') as f:
    out = f.readlines()
    out = out[-2].split('\t')
    # TODO: Handle worst case of sentence having tabs
    return out[2].replace('@', '')


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