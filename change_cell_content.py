
import openpyxl

print("変更するExcelたちが入ってるフォルダパスを入力↓")
children_path = input()

print("親Excelのパスを入力↓")
parent_path = input()

print("親Excelの対象シートを入力↓")
sheet = input()

# ブックを取得
p_book = openpyxl.load_workbook(parent_path)

# シートを取得
シート変数 = ブック変数[シート名]
# セルへ書き込む
シート変数[セル記号] = 書き込む値
シート変数.cell(row=行,column=列).value = 書き込む値