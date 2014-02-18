package com.example.hellogyp;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity
{
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        TextView greeting = (TextView)findViewById(R.id.greeting);
        greeting.setText(stringFromJNI());
    }

    public native String stringFromJNI();

    static {
        System.loadLibrary("_android_jni_hellogyp_jni_gyp");
    }
}
