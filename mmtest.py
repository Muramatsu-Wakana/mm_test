import shutil
import os
import glob  # ライブラリの読み込み

# ------------------------------------------------
# 変数
# ------------------------------------------------
# パスを入力（フォルダのパス）（このフォルダ下のすべての[拡張子]を取得）
path = 'C:\\Users\\u2022087\\Desktop\\Other\\研修'
# 取り出したファイルを入れるフォルダ （空の場合は path と同じディレクトリになるよ）
path_complete = 'C:\\Users\\u2022087'
name_complete = '完成フォルダ'  # 完成したフォルダの名前
extension = 'pdf'  # ターゲットの拡張子

# ------------------------------------------------
# 準備
# ------------------------------------------------


def fileSearch(dir):
    path_list = glob.glob(dir + '\*')       # 指定dir内の全てのファイルを取得

    # パスリストからファイル名を抽出
    all_list = []
    for i in path_list:
        file = os.path.basename(i)
        name, ext = os.path.splitext(file)
        all_list = [i, name, ext]  # 多次元配列 [絶対パス、ファイル名、拡張子]
    return all_list


def fileSearch2(dir, ext):
    path_list = glob.glob(dir + '\*')       # 指定dir内の全てのファイルを取得

    # パスリストからファイル名を抽出
    all_list = []
    for i in path_list:
        file = os.path.basename(i)
        name, ext = os.path.splitext(file)
        all_list.append([i, name, ext])  # 多次元配列 [絶対パス、ファイル名、拡張子]

    list_ext = []

    for a in all_list:
        if extension in a[2]:
            list_ext.append(a)

    return list_ext


# ↑　多次元配列 [絶対パス、ファイル名、拡張子]　を返す

# ------------------------------------------------
# 実行
# ------------------------------------------------
path_comp = path_complete+'\\'+name_complete

# 完成フォルダ作成
try:
    os.mkdir(path_comp)
    print(name_complete+'フォルダが作成されました')
except:
    print('そのフォルダは既に存在します')

list = fileSearch2(path, extension)  # ファイル情報を取得

for a in list:
    # ("コピー元のパス＆ファイル名","コピー先のパス＆ファイル名")
    try:
        shutil.copyfile(a[0], path_comp+'\\'+a[1]+a[2])
        print(a[1]+a[2]+'　をコピーしました')
    except:
        print('そのファイル名は既に存在します')

print('場所：'+path_comp)
