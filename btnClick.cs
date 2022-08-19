using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class btnClick : MonoBehaviour
{
    public List<human> list = new List<human>();

    public struct human
    {
        public int mf;  //性別
        public int height;  //身長

        public string name; //名前
    }

    //Button1のOnClickで呼び出される
    public void Btn1Click()
    {
        //リストに新しく追加（ list[0] ）
        list.Add(new human { mf = 1, height = 160 });

        Debug.Log("ボタン１が押されたよ");
    }

    //Button2のOnClickで呼び出される
    public void BtnClick2()
    {
        //---------------------------------------------------------------------------------
        //ここでlist[0]にnameを追加したい　けど書き方がわからない
        //---------------------------------------------------------------------------------


        Debug.Log("性別：" + list[0].mf + "　　身長：" + list[0].height + "　　名前：" + list[0].name);
    }
}
