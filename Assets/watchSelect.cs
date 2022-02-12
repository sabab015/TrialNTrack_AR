using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;
public class watchSelect : MonoBehaviour
{
    public GameObject watchModel1;
    public GameObject watchModel2;
    public GameObject watchModel3;

    public GameObject w1Window;
    public GameObject w2Window;
    public GameObject w3Window;

    Animation w1WindowAnimation;
    Animation w2WindowAnimation;
    Animation w3WindowAnimation;

    // Start is called before the first frame update
    void Start()
    {
        w1WindowAnimation = w1Window.GetComponent<Animation>();
        w2WindowAnimation = w2Window.GetComponent<Animation>();
        w3WindowAnimation = w3Window.GetComponent<Animation>();
    }

    public void watchOneButtonClicked()
    {
        watchModel1.SetActive(true);
        watchModel2.SetActive(false);
        watchModel3.SetActive(false);

        w1WindowAnimation["w1"].speed = 1;
        w1WindowAnimation.Play();
    }
    public void watchTwoButtonClicked()
    {
        watchModel1.SetActive(false);
        watchModel2.SetActive(true);
        watchModel3.SetActive(false);
        
        w2WindowAnimation["w2"].speed = 1;
        w2WindowAnimation.Play();
    }
    public void watchThreeButtonClicked()
    {
        watchModel1.SetActive(false);
        watchModel2.SetActive(false);
        watchModel3.SetActive(true);

        w3WindowAnimation["w3"].speed = 1;
        w3WindowAnimation.Play();
    }

    public void closeButtonClicked()
    {
        string buttonName = EventSystem.current.currentSelectedGameObject.name;

        if (buttonName== "w1Close")
        {
            w1WindowAnimation["w1"].speed = -1;
            w1WindowAnimation["w1"].time = w1WindowAnimation["w1"].length;
            w1WindowAnimation.Play();
        }
        else if (buttonName == "w2Close")
        {
            w2WindowAnimation["w2"].speed = -1;
            w2WindowAnimation["w2"].time = w2WindowAnimation["w2"].length;
            w2WindowAnimation.Play();
        }
        else if (buttonName == "w3Close")
        {
            w3WindowAnimation["w3"].speed = -1;
            w3WindowAnimation["w3"].time = w3WindowAnimation["w3"].length;
            w3WindowAnimation.Play();
        }

    }



}
