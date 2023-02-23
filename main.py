import csv

class RLE_Decoder:
    def __init__(self, csv_filepath):
        self.csv_filepath = csv_filepath


    def run_RLE_decoder(self):
        with open(self.csv_filepath, 'r') as self.csv:
            self.csvreader = csv.reader(self.csv)
            for row in self.csvreader:
                print(row)



if __name__ == "__main__":
    decoder  = RLE_Decoder("clown_grey_3_rle.csv")
    decoder.run_RLE_decoder()