package com.codenicely.edusmart.helper;

import android.app.Application;
import android.content.Context;
import android.util.Log;


import static com.bumptech.glide.gifdecoder.GifHeaderParser.TAG;

/**
 * Created by meghal on 11/10/16.
 */

public class MyApplication extends Application {

    private static Context context;
    private static String fcm_token;

    @Override
    public void onCreate() {
        super.onCreate();
        context = this;
    /*    FontsOverride.setDefaultFont(this, "DEFAULT", "fonts/comfortaa.ttf");
        FontsOverride.setDefaultFont(this, "MONOSPACE", "fonts/homemade.ttf");
    */
        FontsOverride.setDefaultFont(this, "SERIF", "fonts/nunito.ttf");
        //   FontsOverride.setDefaultFont(this, "SANS_SERIF", "fonts/patrick_hand.ttf");
        //fcm_token = FirebaseInstanceId.getInstance().getToken();
        fcm_token="bfjfwfejfe";

    }

    public static String getFcm_token() {

        Log.d(TAG, "Fcm is " + fcm_token);
        return fcm_token;
    }

    public static Context getContext() {
        return context;
    }


}
