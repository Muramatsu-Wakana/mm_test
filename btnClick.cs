using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class btnClick : MonoBehaviour
{
    public List<human> list = new List<human>();

    public struct human
    {
        public int mf;  //����
        public int height;  //�g��

        public string name; //���O
    }

    //Button1��OnClick�ŌĂяo�����
    public void Btn1Click()
    {
        //���X�g�ɐV�����ǉ��i list[0] �j
        list.Add(new human { mf = 1, height = 160 });

        Debug.Log("�{�^���P�������ꂽ��");
    }

    //Button2��OnClick�ŌĂяo�����
    public void BtnClick2()
    {
        //---------------------------------------------------------------------------------
        //������list[0]��name��ǉ��������@���Ǐ��������킩��Ȃ�
        //---------------------------------------------------------------------------------


        Debug.Log("���ʁF" + list[0].mf + "�@�@�g���F" + list[0].height + "�@�@���O�F" + list[0].name);
    }
}
