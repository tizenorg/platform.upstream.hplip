/*****************************************************************************\
  interp_data_50.h : constant data

  Copyright (c) 1996 - 2001, Hewlett-Packard Co.
  All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:
  1. Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  3. Neither the name of Hewlett-Packard nor the names of its
     contributors may be used to endorse or promote products derived
     from this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND ANY EXPRESS OR IMPLIED
  WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN
  NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
  TO, PATENT INFRINGEMENT; PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
  OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
  ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
\*****************************************************************************/


#ifndef APDK_INTERP_DATA_50_H
#define APDK_INTERP_DATA_50_H

APDK_BEGIN_NAMESPACE

#define     NBANDS3         8
#define NSUBCLASSES3    45
#define     VARIANCE3   ((float) 0.222875)
#define INV_VARIANCE3  ((float) 4.486825)
#define CNST3       ((float) -1.346927)
#define CLUST_VEC_POWER3        ((float) 0.250000)
#define INTERP_FACTOR3          2
#define W3                  1
#define P3                  1
#define BORDER3             3
#define TOTAL_LENGTH3           13
#define INTERP_CLUST_LENGTH3    8
#define FILT_LENGTH3            9
#define HIGH_RES_LENGTH3        4

const float pi3[NSUBCLASSES3] =
{

    0.134087f,  0.021311f,  0.019648f,  0.024394f,  0.034935f,  0.021820f,
    0.019170f,  0.022179f,  0.013944f,  0.012440f,  0.014401f,  0.013066f,
    0.035246f,  0.032467f,  0.014440f,  0.011417f,  0.010087f,  0.020046f,
    0.028311f,  0.017097f,  0.023745f,  0.016038f,  0.022072f,  0.023036f,
    0.028802f,  0.023446f,  0.015276f,  0.022871f,  0.011345f,  0.016940f,
    0.016896f,  0.018755f,  0.016816f,  0.011902f,  0.032550f,  0.024784f,
    0.012820f,  0.023129f,  0.008851f,  0.013391f,  0.018903f,  0.014587f,
    0.011018f,  0.022673f,  0.028847f
};

const float means3[NSUBCLASSES3*NBANDS3] =
{   0.000774f,  0.003593f,  -0.002086f, 0.001974f,  0.001090f,  0.006085f,  0.009383f,  -0.000469f,
    -1.044311f, -0.765389f, -1.175416f, -0.742516f, -0.743477f, -1.186353f, -0.836232f, -1.090520f,
    0.338283f,  -0.774581f, -1.416901f, 0.821453f,  -1.176914f, 1.000631f,  0.568897f,  -0.702795f,
    -0.058699f, -0.462371f, -2.470061f, -0.071035f, -0.536233f, -0.420050f, -0.069105f, -0.048716f,
    -0.064657f, 0.027666f,  -0.037047f, -0.181144f, -0.189198f, -1.650089f, -1.774374f, -1.686162f,
    2.455220f,  0.387699f,  0.019051f,  0.463026f,  -0.013956f, 0.029817f,  -0.016442f, -0.026744f,
    -1.025410f, 0.420109f,  1.194990f,  -1.235820f, 1.152444f,  -1.312478f, -0.425713f, 0.939458f,
    0.026192f,  0.338014f,  2.422950f,  -0.032347f, 0.482617f,  -0.025641f, -0.039135f, 0.016212f,
    0.006554f,  0.270283f,  2.149937f,  -0.037302f, 2.076884f,  0.136553f,  0.105003f,  1.754475f,
    2.173123f,  0.560274f,  0.070122f,  0.632557f,  0.465478f,  0.111966f,  0.484268f,  2.009682f,
    0.219957f,  1.467974f,  1.995528f,  -0.398120f, 1.589261f,  -0.388413f, -0.387530f, 0.241743f,
    -0.270451f, -1.699654f, -2.265285f, 0.203561f,  -1.618941f, -0.037976f, 0.210997f,  -0.186532f,
    -0.048094f, -0.166164f, -1.663206f, 0.017631f,  -1.772144f, -0.103216f, -0.225762f, -1.681172f,
    1.730204f,  1.737262f,  1.593460f,  0.181974f,  0.152116f,  -0.109539f, -0.141882f, -0.056063f,
    -0.230952f, 0.275236f,  0.072651f,  -1.635954f, 0.262965f,  -2.168830f, -1.615753f, -0.222218f,
    1.079399f,  0.244801f,  1.199122f,  1.162549f,  1.279812f,  0.986483f,  0.184212f,  1.201325f,
    -0.560544f, -0.524704f, 0.352553f,  -0.562952f, 1.635709f,  -0.059114f, 1.425960f,  1.849587f,
    -0.010279f, -0.003744f, -0.028509f, -0.018431f, -0.402123f, -0.066750f, -0.386577f, -2.443244f,
    -1.723825f, -1.820417f, -1.734338f, -0.163968f, -0.219895f, -0.017193f, 0.020660f,  -0.088216f,
    -1.400438f, -0.718206f, 0.598797f,  -1.257422f, 0.914653f,  -0.834154f, 0.557207f,  0.997338f,
    0.029900f,  -0.014535f, -0.011792f, 0.387747f,  -0.014952f, 2.436290f,  0.383958f,  0.004128f,
    -0.074886f, 0.160291f,  -0.237074f, 0.174993f,  -1.615974f, -0.221347f, -1.553910f, -2.203187f,
    -0.942591f, -1.190646f, -1.277313f, 0.384835f,  -0.446394f, 1.155884f,  1.122480f,  0.880156f,
    0.271327f,  0.837829f,  1.121860f,  -0.692023f, 0.557900f,  -1.368542f, -0.992892f, -0.465196f,
    -0.000725f, -0.066347f, 0.033421f,  0.271319f,  0.074580f,  1.858489f,  1.790623f,  1.505258f,
    -0.206268f, 0.132244f,  1.368347f,  -0.262435f, 1.419442f,  -0.173428f, 0.156229f,  1.361413f,
    0.249327f,  0.030119f,  0.081970f,  0.023521f,  0.591752f,  0.641430f,  1.702287f,  2.259731f,
    1.259956f,  0.251106f,  -1.004476f, 1.239093f,  -1.117822f, 1.105386f,  -0.194298f, -1.129517f,
    1.116877f,  1.183586f,  1.026623f,  0.195173f,  0.209617f,  1.147194f,  1.211576f,  1.212144f,
    -2.510197f, -0.349424f, 0.026320f,  -0.373562f, 0.041303f,  0.010736f,  0.029276f,  0.006751f,
    -0.953774f, -0.891946f, -0.603629f, -0.434015f, 0.662118f,  0.986387f,  1.303651f,  1.435651f,
    0.326236f,  -0.257195f, -0.147855f, 1.640779f,  -0.295173f, 2.109913f,  1.451703f,  0.103715f,
    2.087317f,  1.528896f,  0.209018f,  1.569349f,  -0.233623f, 0.276365f,  -0.232146f, -0.127082f,
    0.487855f,  0.039350f,  0.511064f,  0.061401f,  1.817653f,  0.086290f,  0.785898f,  2.408901f,
    1.679159f,  0.178437f,  -0.001353f, 1.793388f,  -0.086769f, 1.683560f,  0.201818f,  -0.006799f,
    1.141604f,  1.130186f,  0.999398f,  0.229770f,  -0.274429f, -1.043950f, -1.194934f, -1.220279f,
    -1.988732f, -0.426505f, -0.109894f, -0.488769f, -0.708144f, -0.076649f, -0.560441f, -2.158441f,
    -0.045908f, -0.068920f, -0.499930f, -0.476361f, -0.090959f, -2.472999f, -0.497707f, -0.053086f,
    0.493526f,  1.809131f,  2.396506f,  0.043945f,  0.786366f,  0.614150f,  0.043658f,  0.055845f,
    -2.321377f, -1.448210f, -0.237279f, -1.517980f, 0.024960f,  -0.308394f, 0.004862f,  -0.375930f,
    1.079487f,  0.684766f,  -0.280942f, 0.699966f,  -0.957105f, -0.107189f, -0.868223f, -1.323501f,
    -1.626288f, -1.425036f, -0.791911f, -1.011117f, 0.456523f,  0.115604f,  0.579521f,  0.700434f,
    0.087343f,  0.388898f,  1.972170f,  0.596996f,  0.527294f,  2.121683f,  0.562680f,  0.103259f,
    -0.015322f, -0.019346f, 0.031279f,  -0.035924f, 0.363621f,  0.004034f,  0.292051f,  2.362132f,
    -1.657692f, -0.143410f, 0.030477f,  -1.789348f, 0.072525f,  -1.738594f, -0.258791f, -0.077726f

};



const float joint_means3[NSUBCLASSES3*TOTAL_LENGTH3] =
{-0.569017f,
-0.592667f,    -0.532251f,    -0.533552f,    91.392197f,    91.432030f,    91.380524f,
91.478882f,    91.409416f,    91.421944f,    91.493507f,    91.523048f,    91.436142f,
5.571358f,    5.433944f,    5.135954f,    5.441774f,    95.298454f,    99.144691f,
94.238480f,    100.177010f,    113.276299f,    100.370522f,    93.951485f,    98.835159f,
95.179161f,    2.617124f,    -8.117904f,    8.099975f,    -2.373677f,    99.011528f,
87.405159f,    79.455757f,    105.221268f,    95.564682f,    82.333443f,    107.339516f,
101.415665f,    87.523445f,    1.424042f,    0.917556f,    0.920758f,    1.525805f,
119.968521f,    113.834908f,    93.340248f,    119.746132f,    121.602486f,    113.576851f,
116.983887f,    119.928452f,    120.351059f,    7.603677f,    7.543176f,    -0.585176f,
-0.781502f,    123.565308f,    125.070862f,    123.865517f,    121.594925f,    125.237671f,
121.372185f,    97.513763f,    96.125275f,    96.919067f,    -1.331300f,    -2.138124f,
-2.018178f,    -2.096316f,    99.314339f,    77.261803f,    71.717735f,    78.142349f,
70.875839f,    70.950912f,    71.936111f,    70.862465f,    70.617989f,    -8.014888f,
11.075225f,    -11.452845f,    7.494443f,    78.748947f,    98.882088f,    112.406013f,
75.759773f,    94.514481f,    111.610947f,    74.622856f,    89.485092f,    108.127876f,
-1.952583f,    -1.344249f,    -2.002568f,    -2.008949f,    71.729599f,    76.722618f,
98.642471f,    70.899178f,    70.813446f,    77.892159f,    70.545074f,    70.513885f,
71.322296f,    -13.498682f,    -5.279373f,    -13.301547f,    -6.530796f,    67.035637f,
74.070358f,    137.483719f,    65.706306f,    66.501457f,    135.201691f,    68.068069f,
70.333176f,    126.416885f,    -2.421132f,    -7.263986f,    -7.113289f,    -5.041696f,
113.511879f,    92.299118f,    82.014198f,    93.077629f,    78.905998f,    89.579971f,
82.713440f,    89.633247f,    110.730766f,    -7.695601f,    8.778397f,    -13.626282f,
-7.350642f,    86.419464f,    107.533638f,    118.287590f,    75.017532f,    81.295914f,
110.057587f,    73.994385f,    74.698235f,    87.015480f,    10.047956f,    -13.062446f,
16.113504f,    11.422572f,    122.734695f,    92.693207f,    78.726280f,    136.608215f,
132.787689f,    94.179359f,    132.055710f,    136.875946f,    125.348862f,    9.224700f,
-0.109693f,    8.965702f,    -0.078194f,    115.766251f,    112.862633f,    81.901588f,
116.770088f,    116.841194f,    80.694397f,    115.074623f,    112.464111f,    81.732422f,
-0.431740f,    -0.687818f,    -8.019328f,    -7.777046f,    110.912521f,    111.521744f,
109.288757f,    86.766777f,    83.508438f,    86.315483f,    82.502731f,    81.744019f,
82.964638f,    7.614752f,    15.064453f,    -11.623741f,    8.475021f,    119.371834f,
131.461380f,    128.155228f,    94.235275f,    127.049324f,    131.303925f,    82.234612f,
95.401711f,    120.397751f,    -6.302689f,    -5.910920f,    -6.547348f,    -6.058825f,
99.441788f,    88.666321f,    100.618683f,    100.768311f,    82.404396f,    102.045547f,
98.608253f,    87.694519f,    100.009857f,    -17.036495f,    -6.378878f,    -10.414292f,
15.038725f,    72.114906f,    74.113663f,    91.563385f,    72.744331f,    83.816856f,
116.170692f,    82.362083f,    111.237984f,    121.416061f,    0.414496f,    0.749763f,
0.770419f,    0.529369f,    120.045616f,    120.292374f,    120.079086f,    120.000946f,
120.662018f,    114.732941f,    119.496468f,    114.432312f,    95.465790f,    -0.047362f,
-0.496625f,    8.377548f,    7.852504f,    96.215767f,    95.152092f,    96.173256f,
124.467606f,    127.835419f,    123.311234f,    126.523270f,    127.219604f,    125.338181f,
-9.018794f,    3.995118f,    -3.569654f,    8.789133f,    79.912880f,    89.855011f,
104.201942f,    81.839714f,    97.283287f,    108.731216f,    86.471237f,    102.783073f,
109.948669f,    -1.823330f,    -1.852720f,    -1.546260f,    -1.880081f,    72.081467f,
71.325989f,    71.009010f,    77.561722f,    71.134575f,    71.143837f,    99.420532f,
77.284317f,    71.668335f,    13.929065f,    7.956630f,    8.870374f,    -10.052946f,
125.737823f,    130.778152f,    120.724350f,    130.647171f,    128.013351f,    95.409035f,
121.004829f,    96.383324f,    82.803116f,    -5.556594f,    -8.549821f,    7.806454f,
4.750080f,    91.123817f,    88.292786f,    87.096481f,    106.440826f,    102.886307f,
98.477074f,    116.702499f,    116.316559f,    113.158890f,    1.075539f,    5.265429f,
-5.829627f,    -1.670283f,    103.415489f,    109.201225f,    111.960876f,    94.489799f,
100.937698f,    105.862770f,    87.691956f,    91.334579f,    96.183907f,    -8.266474f,
-8.448220f,    -0.802359f,    -1.792390f,    81.980453f,    80.811188f,    81.881554f,
86.368500f,    81.779594f,    83.906342f,    113.921211f,    113.435555f,    109.066956f,
-5.534815f,    0.411996f,    -5.401955f,    0.668718f,    70.415718f,    74.712982f,
88.463638f,    69.656181f,    72.653130f,    89.422325f,    70.497787f,    74.922699f,
88.350533f,    -6.634558f,    -7.243901f,    -5.026807f,    -1.170539f,    81.272621f,
78.884071f,    79.765373f,    78.930000f,    77.668007f,    87.874817f,    90.459694f,
108.092659f,    115.805992f,    12.936280f,    -12.199434f,    11.127541f,    -13.687916f,
105.847946f,    87.855843f,    68.378708f,    105.886459f,    85.538193f,    66.909096f,
103.999008f,    83.844185f,    66.849159f,    -6.029956f,    -5.981055f,    -6.247091f,
-6.074353f,    108.351288f,    109.286522f,    107.517570f,    95.627098f,    90.747322f,
95.624100f,    108.178535f,    109.406937f,    108.333992f,    0.576806f,    0.499227f,
0.344188f,    0.286852f,    95.710686f,    117.635460f,    123.376480f,    117.645851f,
123.572441f,    123.630150f,    123.043686f,    123.276077f,    123.182358f,    -9.367361f,
-5.822471f,    2.340962f,    6.929045f,    84.255791f,    85.353493f,    88.596397f,
91.730324f,    95.721077f,    101.984619f,    107.772736f,    111.527061f,    112.834869f,
-7.752755f,    -12.788501f,    7.672995f,    -9.399925f,    85.713646f,    73.873901f,
74.654320f,    109.969421f,    78.359344f,    73.395462f,    119.231781f,    105.176338f,
81.158844f,    6.506885f,    -8.369875f,    -8.087216f,    -12.377110f,    118.216179f,
107.354614f,    85.525955f,    108.480766f,    80.080399f,    76.482391f,    86.772003f,
76.417801f,    77.406715f,    -8.335778f,    -8.759060f,    -9.785326f,    -1.862754f,
79.101120f,    72.741394f,    84.546692f,    73.024803f,    70.191154f,    113.874413f,
73.086609f,    87.855972f,    126.313011f,    -1.089821f,    -7.504702f,    -0.784354f,
-7.460814f,    92.638008f,    64.828102f,    61.524342f,    94.584999f,    61.890564f,
60.457340f,    92.596802f,    65.193420f,    61.392639f,    7.224984f,    5.508367f,
-6.601244f,    -8.299099f,    119.172958f,    119.234459f,    117.170547f,    106.564400f,
104.419556f,    101.939377f,    91.159096f,    89.243958f,    88.913170f,    4.834817f,
6.572627f,    6.972660f,    0.248389f,    91.959816f,    115.464470f,    122.800743f,
114.467285f,    127.623825f,    110.708786f,    123.693909f,    112.996857f,    91.340538f,
1.564369f,    1.211442f,    0.702830f,    1.520065f,    120.967758f,    120.471642f,
116.924500f,    114.367996f,    122.219948f,    120.325874f,    94.351334f,    114.283783f,
120.916695f,    -7.336087f,    -0.728319f,    -8.558440f,    -9.466346f,    89.045273f,
113.133560f,    123.105583f,    79.906868f,    76.912331f,    92.106407f,    88.548775f,
80.305260f,    79.564484f,    -6.223439f,    9.556105f,    8.335138f,    11.464046f,
81.604156f,    99.020416f,    122.144852f,    96.974823f,    129.496078f,    128.028473f,
119.025749f,    127.608276f,    120.524513f,    5.649610f,    -0.488222f,    0.112771f,
-5.868335f,    107.334602f,    102.935028f,    93.884056f,    103.163963f,    96.557159f,
87.643944f,    95.242966f,    88.395599f,    83.639801f,    -7.558787f,    -0.476352f,
3.969364f,    8.754784f,    88.680267f,    91.705399f,    97.700638f,    97.635132f,
108.679947f,    112.947777f,    109.305885f,    115.758072f,    117.416862f,    -6.848458f,
-4.182240f,    -3.552881f,    -6.959355f,    80.924568f,    87.599205f,    108.441681f,
90.706146f,    77.277069f,    88.977470f,    110.651855f,    89.479492f,    80.840805f,
-1.555507f,    -1.539033f,    -1.609181f,    -1.199703f,    72.196388f,    72.513420f,
72.907913f,    72.419037f,    72.624451f,    77.853828f,    72.784454f,    77.307564f,
98.581871f,    0.992525f,    9.604681f,    0.665015f,    9.211377f,    74.333717f,
109.724792f,    112.634926f,    73.194771f,    112.807877f,    113.447563f,    73.603554f,
108.458832f,    111.487160f
};

const float filter3[NSUBCLASSES3*FILT_LENGTH3*HIGH_RES_LENGTH3] =
{-0.038539f,
-0.006377f, -0.014330f, 0.047676f,  0.100775f,  0.091890f,  -0.300097f,
-0.313949f, -0.028815f, -0.028053f, 0.052156f,  -0.009875f, 0.096480f,
-0.303045f, 0.099607f,  -0.298992f, 0.425550f,  0.408621f,  0.439068f,
0.431584f,  -0.287630f, 0.101664f,  -0.315186f, 0.100685f,  -0.002751f,
0.041112f,  -0.036271f, -0.021252f, -0.311411f, -0.288203f, 0.078438f,
0.100573f,  0.045634f,  -0.018256f, -0.004139f, -0.037185f, 0.037846f,
-0.094659f, -0.082729f, 0.106169f,  0.128023f,  0.194925f,  -0.374994f,
-0.327435f, -0.065959f, 0.005289f,  0.164576f,  -0.080647f, 0.153420f,
-0.357661f, 0.167628f,  -0.313016f, 0.373973f,  0.357408f,  0.362472f,
0.346208f,  -0.336954f, 0.177288f,  -0.344828f, 0.147837f,  -0.079879f,
0.136531f,  0.030287f,  -0.075772f, -0.331317f, -0.355312f, 0.180272f,
0.155402f,  0.109490f,  -0.069536f, -0.108796f, 0.029849f,  0.211609f,
-0.151922f, 0.006219f,  -0.094823f, -0.022478f, 0.387082f,  -0.444967f,
-0.301156f, 0.058780f,  -0.199739f, 0.222122f,  -0.064855f, 0.068008f,
-0.359451f, 0.310457f,  -0.467473f, 0.607806f,  0.234437f,  0.198337f,
0.676615f,  -0.446353f, 0.307628f,  -0.333007f, 0.031864f,  -0.035179f,
0.107025f,  -0.047970f, 0.012583f,  -0.374403f, -0.395650f, 0.306657f,
0.018535f,  -0.075709f, 0.076843f,  -0.232489f, 0.197227f,  0.014156f,
-0.014866f, -0.038554f, 0.014511f,  -0.044734f, 0.102592f,  -0.221716f,
-0.265067f, 0.043170f,  -0.122283f, 0.106632f,  0.044143f,  0.062062f,
-0.399096f, 0.216543f,  -0.274992f, 0.435559f,  0.640194f,  0.030215f,
0.451540f,  -0.233589f, 0.090198f,  -0.204101f, -0.056299f, -0.002206f,
0.143431f,  -0.081150f, -0.017569f, -0.308730f, -0.399827f, 0.225155f,
0.067090f,  0.031726f,  -0.048616f, -0.027466f, 0.032326f,  0.029253f,
0.013799f,  -0.062027f, 0.043405f,  0.164658f,  0.135356f,  -0.349309f,
-0.354348f, -0.002888f, 0.041562f,  0.066073f,  -0.058247f, 0.027416f,
-0.262536f, 0.176518f,  -0.291665f, 0.323808f,  0.310224f,  0.432907f,
0.398017f,  -0.308968f, 0.001312f,  -0.286425f, 0.235222f,  -0.082403f,
0.096378f,  -0.022362f, -0.001621f, -0.287247f, -0.330346f, 0.105533f,
0.074766f,  0.102766f,  -0.042037f, -0.036963f, -0.024264f, -0.082110f,
0.021523f,  0.007256f,  0.055798f,  0.078652f,  -0.052060f, -0.226890f,
-0.192233f, -0.085468f, 0.082933f,  0.034081f,  -0.034248f, 0.049751f,
-0.223606f, -0.046080f, -0.168982f, 0.816598f,  0.365437f,  0.381294f,
0.024015f,  -0.439763f, 0.057289f,  -0.269818f, 0.237595f,  -0.028636f,
-0.003287f, 0.062391f,  -0.038873f, -0.364169f, -0.239898f, 0.056306f,
0.132044f,  0.054477f,  -0.011338f, -0.002422f, -0.018442f, 0.223555f,
-0.317230f, 0.188120f,  -0.151293f, 0.086944f,  0.158705f,  -0.267532f,
-0.414706f, 0.015522f,  -0.066588f, 0.076893f,  -0.026280f, 0.100254f,
-0.377826f, 0.277492f,  -0.472827f, 0.332768f,  0.522778f,  0.081638f,
0.799384f,  -0.384792f, 0.187138f,  -0.293827f, 0.045525f,  -0.004015f,
0.113908f,  -0.093851f, -0.007372f, -0.258776f, -0.357762f, 0.237904f,
0.039333f,  -0.094290f, 0.107982f,  -0.190837f, 0.160000f,  0.044950f,
0.017068f,  -0.087331f, 0.024120f,  -0.046207f, 0.082042f,  -0.193270f,
-0.251483f, 0.016711f,  -0.087349f, 0.054266f,  0.011762f,  0.070761f,
-0.400174f, 0.236681f,  -0.314893f, 0.351154f,  0.734474f,  0.045844f,
0.479364f,  -0.202191f, 0.055457f,  -0.182188f, -0.051137f, -0.013923f,
0.057497f,  -0.010780f, -0.010385f, -0.251828f, -0.395527f, 0.146461f,
0.078176f,  0.026793f,  -0.063364f, -0.014208f, 0.031309f,  0.195676f,
-0.272931f, 0.159328f,  -0.083343f, -0.176654f, 0.268300f,  -0.242208f,
-0.200756f, 0.035675f,  -0.108883f, 0.124737f,  -0.057824f, 0.174403f,
-0.337902f, 0.184825f,  -0.371331f, 0.008686f,  0.800090f,  -0.049191f,
0.751294f,  -0.171097f, -0.031303f, -0.181403f, -0.055480f, -0.002609f,
0.056020f,  0.019620f,  -0.063656f, -0.190335f, -0.302646f, -0.063810f,
0.179970f,  0.001563f,  0.008303f,  -0.080241f, -0.014801f, -0.225420f,
0.043172f,  0.011874f,  0.174858f,  0.281979f,  -0.143768f, -0.235249f,
-0.299497f, -0.164309f, 0.163043f,  0.008138f,  -0.023346f, 0.275668f,
-0.259545f, -0.140663f, -0.278952f, 0.331520f,  0.578112f,  0.510491f,
0.201095f,  -0.284796f, -0.135826f, -0.221269f, 0.267243f,  -0.105222f,
-0.035177f, 0.163730f,  -0.076207f, -0.262958f, -0.247158f, -0.144369f,
0.241386f,  0.164747f,  0.024927f,  0.031004f,  -0.214805f, 0.170571f,
-0.128602f, -0.080023f, -0.002011f, -0.103536f, 0.255655f,  -0.201626f,
-0.351362f, 0.048403f,  -0.205119f, 0.132327f,  0.028883f,  0.074047f,
-0.569580f, 0.400581f,  -0.290180f, 0.410293f,  1.174623f,  -0.461240f,
0.504287f,  -0.338923f, 0.177329f,  -0.172856f, -0.077635f, -0.018366f,
0.021709f,  -0.015637f, 0.062549f,  -0.274590f, -0.606581f, 0.445955f,
0.007324f,  0.029480f,  -0.096463f, -0.089122f, 0.118637f,  0.172921f,
-0.023366f, -0.167288f, -0.010280f, -0.145919f, 0.437895f,  -0.295632f,
-0.352554f, 0.091878f,  -0.433384f, 0.261227f,  0.110753f,  -0.006829f,
-0.565171f, 0.415717f,  -0.231244f, 0.451488f,  0.556397f,  -0.141596f,
0.485789f,  -0.341071f, 0.499413f,  -0.281441f, -0.191709f, 0.093826f,
0.227455f,  -0.224415f, 0.024399f,  -0.317060f, -0.555758f, 0.447157f,
0.033543f,  -0.016598f, -0.094330f, -0.063069f, 0.108099f,  0.074997f,
-0.075776f, 0.011205f,  0.028938f,  -0.088643f, 0.302885f,  -0.311704f,
-0.219449f, -0.013551f, -0.114632f, 0.145831f,  -0.066035f, 0.139388f,
-0.365222f, 0.169996f,  -0.323064f, 0.377941f,  0.368001f,  0.334946f,
0.332769f,  -0.350325f, 0.127974f,  -0.328386f, 0.104849f,  0.050448f,
0.059929f,  0.046040f,  -0.121134f, -0.364001f, -0.236433f, -0.059155f,
0.360426f,  0.129808f,  -0.050684f, -0.051941f, -0.083811f, -0.062922f,
-0.021130f, -0.013934f, 0.080966f,  -0.001278f, -0.018578f, -0.200779f,
-0.199021f, 0.020747f,  -0.003021f, 0.001041f,  -0.084133f, 0.233064f,
-0.303245f, -0.065640f, -0.253698f, 0.684579f,  0.722319f,  0.164290f,
0.114581f,  -0.346307f, 0.143139f,  -0.204638f, -0.003047f, -0.165914f,
-0.023076f, 0.103756f,  0.076082f,  -0.368865f, -0.381985f, 0.177470f,
0.176172f,  0.029599f,  -0.088425f, 0.001886f,  0.060270f,  0.165462f,
-0.084299f, -0.092631f, -0.030557f, -0.054623f, 0.396785f,  -0.478884f,
-0.261572f, 0.135054f,  -0.226577f, 0.146775f,  0.023170f,  -0.101874f,
-0.292678f, 0.406803f,  -0.379223f, 0.468669f,  -0.050527f, 0.573784f,
0.468039f,  -0.367056f, 0.385542f,  -0.479997f, 0.075179f,  0.059797f,
0.236400f,  -0.348575f, 0.100431f,  -0.383957f, -0.335591f, 0.441099f,
-0.108192f, 0.065435f,  -0.074598f, -0.126676f, 0.101009f,  0.037006f,
-0.118981f, 0.005055f,  0.040852f,  0.129756f,  0.090297f,  -0.277477f,
-0.312564f, -0.117482f, 0.058118f,  0.047260f,  -0.043996f, 0.017865f,
-0.222113f, 0.012222f,  -0.200350f, 0.403085f,  0.422116f,  0.412928f,
0.434283f,  -0.229642f, 0.001362f,  -0.210729f, 0.056728f,  -0.023715f,
0.057394f,  0.022204f,  -0.104058f, -0.273857f, -0.298585f, 0.100519f,
0.090161f,  0.048206f,  0.002680f,  -0.123781f, 0.031976f,  -0.091056f,
-0.008982f, -0.014470f, 0.165106f,  0.563916f,  -0.022556f, -0.238121f,
-0.717396f, -0.127001f, 0.196403f,  -0.046102f, -0.087218f, 0.518930f,
-0.315263f, 0.054334f,  -0.607986f, -0.655202f, 0.635625f,  0.459923f,
1.164114f,  -0.189307f, -0.124433f, -0.383164f, 0.259866f,  -0.051335f,
-0.018577f, 0.217040f,  -0.190823f, -0.140183f, -0.365720f, -0.129350f,
0.233518f,  0.139157f,  0.032565f,  0.073984f,  -0.209769f, -0.063082f,
-0.047104f, 0.044894f,  0.084191f,  0.220882f,  0.135381f,  -0.396614f,
-0.372962f, 0.035591f,  0.018929f,  0.039776f,  -0.094316f, 0.238802f,
-0.315182f, 0.062417f,  -0.357961f, -0.101969f, 0.502500f,  0.456624f,
0.710217f,  -0.218455f, -0.067125f, -0.218651f, 0.088901f,  -0.041690f,
-0.020859f, 0.035555f,  -0.025603f, -0.159360f, -0.255471f, -0.054359f,
0.078487f,  0.092441f,  0.046868f,  0.027443f,  -0.115207f, -0.065296f,
-0.032188f, -0.020255f, 0.139151f,  0.090674f,  0.083170f,  -0.301431f,
-0.327831f, 0.009755f,  -0.021837f, 0.071962f,  -0.061453f, 0.220716f,
-0.281490f, -0.008946f, -0.285064f, 0.454359f,  0.393610f,  0.292292f,
0.290638f,  -0.300812f, 0.269453f,  -0.289263f, -0.009589f, -0.084388f,
0.062668f,  0.044321f,  0.028924f,  -0.376310f, -0.381285f, 0.168354f,
0.152308f,  0.079864f,  -0.066482f, -0.001408f, 0.030103f,  -0.227105f,
0.116332f,  -0.115685f, 0.230501f,  0.386250f,  -0.038951f, -0.273956f,
-0.407767f, -0.168184f, 0.177680f,  -0.133099f, 0.063340f,  0.316902f,
-0.489064f, 0.050083f,  -0.318527f, 0.253635f,  0.581441f,  0.771489f,
0.133429f,  -0.361661f, 0.088077f,  -0.506916f, 0.343027f,  0.088038f,
-0.069976f, 0.170115f,  -0.247037f, -0.386423f, -0.347440f, -0.002188f,
0.284998f,  0.103964f,  -0.028559f, 0.048493f,  -0.097583f, 0.005920f,
-0.062874f, -0.017118f, 0.053518f,  0.115878f,  0.169953f,  -0.407580f,
-0.308633f, -0.019012f, 0.018014f,  0.028070f,  0.001222f,  -0.040532f,
-0.148765f, 0.026506f,  -0.207908f, 0.376635f,  0.038171f,  0.835131f,
0.350211f,  -0.285202f, 0.162576f,  -0.399446f, 0.101540f,  0.026254f,
0.050405f,  -0.081267f, 0.016201f,  -0.237212f, -0.176654f, 0.044385f,
-0.036973f, 0.053835f,  -0.056335f, -0.029641f, 0.028929f,  -0.257641f,
0.068391f,  0.047737f,  0.212577f,  0.364318f,  -0.017966f, -0.246723f,
-0.471869f, -0.104872f, 0.177301f,  -0.045693f, -0.081880f, 0.376280f,
-0.270632f, -0.009161f, -0.455878f, 0.080904f,  0.452889f,  0.474998f,
0.405000f,  -0.312015f, -0.132134f, -0.320047f, 0.402063f,  -0.107119f,
-0.035797f, 0.167391f,  -0.069024f, -0.346466f, -0.316509f, -0.171961f,
0.464877f,  0.263527f,  0.065597f,  0.086810f,  -0.364571f, 0.088134f,
0.034978f,  -0.167886f, 0.010731f,  0.157490f,  0.337221f,  -0.429487f,
-0.505035f, -0.081898f, -0.125972f, 0.194588f,  0.020214f,  0.054692f,
-0.345033f, 0.239559f,  -0.358633f, 0.574842f,  0.227677f,  0.306788f,
0.644879f,  -0.258533f, 0.292181f,  -0.411414f, -0.003173f, -0.017793f,
0.077829f,  -0.050437f, -0.009678f, -0.456902f, -0.325057f, 0.230977f,
0.091961f,  -0.057946f, -0.171632f, 0.081214f,  0.105238f,  0.100588f,
-0.049030f, -0.095920f, 0.014710f,  0.060972f,  0.222467f,  -0.301101f,
-0.414350f, -0.035239f, -0.060226f, 0.087387f,  0.003123f,  0.020389f,
-0.406161f, 0.284406f,  -0.312259f, 0.613758f,  0.390717f,  0.201299f,
0.524320f,  -0.351306f, 0.261104f,  -0.373183f, 0.040473f,  0.031402f,
0.163447f,  -0.132031f, -0.047133f, -0.445181f, -0.370438f, 0.287869f,
0.091249f,  0.003770f,  -0.157141f, 0.043023f,  0.100826f,  0.127044f,
0.081631f,  -0.167687f, -0.021388f, 0.225642f,  0.218065f,  -0.428301f,
-0.419011f, 0.005990f,  0.069357f,  0.036948f,  -0.097539f, -0.121056f,
-0.286186f, 0.262259f,  -0.269583f, 0.116073f,  0.062108f,  0.745855f,
0.740329f,  -0.205973f, -0.003648f, -0.353223f, 0.166048f,  0.024368f,
0.109632f,  -0.086132f, -0.039239f, -0.200049f, -0.182107f, -0.000573f,
-0.045871f, -0.013298f, -0.108094f, 0.018849f,  0.013874f,  0.085701f,
-0.133404f, 0.059287f,  -0.003722f, 0.025092f,  0.165576f,  -0.256433f,
-0.355102f, -0.057631f, -0.014532f, 0.035498f,  0.009624f,  0.263768f,
-0.441111f, 0.219099f,  -0.464863f, 0.039621f,  0.777472f,  0.093270f,
0.799600f,  -0.210619f, 0.001037f,  -0.234910f, 0.027800f,  0.065859f,
-0.031514f, 0.124430f,  -0.150805f, -0.272043f, -0.313766f, -0.028215f,
0.188333f,  0.045296f,  -0.006052f, -0.026126f, -0.046757f, -0.152273f,
-0.056162f, 0.031983f,  0.183826f,  0.235771f,  0.074555f,  -0.290660f,
-0.381700f, -0.014400f, 0.147286f,  0.002715f,  -0.165268f, 0.238820f,
-0.157154f, 0.040983f,  -0.518281f, 0.024003f,  0.328874f,  0.574054f,
0.703917f,  -0.197078f, -0.184095f, -0.267343f, 0.249694f,  -0.112289f,
-0.022590f, 0.022108f,  0.049073f,  -0.178447f, -0.248466f, -0.097409f,
0.066510f,  0.126196f,  0.093036f,  -0.010638f, -0.163378f, -0.040780f,
-0.004616f, -0.016181f, 0.069127f,  0.093695f,  0.131924f,  -0.440716f,
-0.219132f, -0.388849f, 0.277741f,  -0.234441f, 0.248210f,  0.082317f,
-0.286888f, -0.027784f, -0.231906f, 0.968896f,  -0.117015f, 1.100811f,
-0.219476f, -0.477928f, 0.280962f,  -0.555048f, 0.320672f,  0.061056f,
-0.020941f, 0.119322f,  -0.132517f, -0.289841f, -0.297186f, 0.158228f,
0.105961f,  -0.062673f, 0.070626f,  -0.157549f, 0.088666f,  0.029685f,
-0.011507f, -0.097330f, 0.052632f,  0.060325f,  0.033389f,  -0.259619f,
-0.257504f, -0.017093f, 0.045234f,  0.031317f,  -0.111592f, 0.131943f,
-0.271723f, 0.066545f,  -0.297126f, 0.405258f,  0.413017f,  0.435310f,
0.447407f,  -0.284218f, 0.091921f,  -0.277713f, 0.106695f,  -0.142680f,
0.031491f,  0.077168f,  -0.000435f, -0.226168f, -0.216700f, 0.000970f,
0.017138f,  0.031209f,  -0.122206f, 0.014423f,  0.040314f,  -0.117203f,
0.042837f,  0.052516f,  0.090925f,  0.089645f,  -0.084481f, -0.234264f,
-0.185552f, -0.066335f, 0.049812f,  0.036655f,  -0.034070f, 0.088912f,
-0.253365f, -0.052777f, -0.202749f, 0.755617f,  0.390916f,  0.444148f,
-0.012960f, -0.356229f, 0.076936f,  -0.340917f, 0.212843f,  -0.041965f,
0.089074f,  -0.028386f, -0.041977f, -0.365181f, -0.343176f, 0.105890f,
0.188486f,  0.000703f,  0.029761f,  0.015733f,  -0.007062f, -0.083699f,
-0.051566f, -0.008131f, 0.149960f,  0.378373f,  0.123415f,  -0.526310f,
-0.429972f, 0.048868f,  0.169094f,  -0.041202f, -0.192173f, 0.275946f,
-0.220524f, 0.014452f,  -0.453918f, 0.018658f,  0.445547f,  0.832657f,
0.473415f,  -0.308061f, -0.020804f, -0.369992f, 0.292199f,  -0.200860f,
-0.099155f, 0.138097f,  0.085523f,  -0.247602f, -0.375975f, -0.013997f,
0.180318f,  0.112575f,  0.032685f,  -0.025856f, -0.107123f, 0.160017f,
-0.111838f, -0.059581f, -0.036245f, 0.043310f,  0.484925f,  -0.730721f,
-0.175829f, 0.013286f,  -0.144975f, 0.158750f,  -0.006119f, -0.171841f,
-0.167615f, 0.213843f,  -0.294353f, 0.446332f,  -0.434399f, 1.177720f,
0.382003f,  -0.292792f, 0.425409f,  -0.597335f, 0.098465f,  0.048768f,
0.141034f,  -0.256730f, 0.102251f,  -0.271365f, -0.212339f, 0.287661f,
-0.214837f, 0.025042f,  -0.027244f, -0.168708f, 0.143563f,  -0.218553f,
0.070602f,  0.056636f,  0.117598f,  0.229367f,  -0.147797f, -0.286600f,
-0.200392f, -0.112789f, 0.123540f,  0.032974f,  -0.094710f, 0.207712f,
-0.308633f, -0.162789f, -0.152930f, 0.961005f,  0.396529f,  0.461616f,
-0.200157f, -0.603361f, 0.030870f,  -0.229512f, 0.410930f,  -0.031579f,
-0.001434f, 0.132325f,  -0.159370f, -0.565002f, -0.173174f, -0.024711f,
0.374993f,  0.166644f,  0.003343f,  0.017942f,  -0.145456f, -0.222910f,
0.017597f,  -0.032838f, 0.236387f,  0.219523f,  -0.037341f, -0.141779f,
-0.431705f, -0.082738f, 0.034822f,  -0.020310f, 0.006781f,  0.274026f,
-0.274250f, 0.027123f,  -0.336656f, -0.031077f, 0.648320f,  0.381077f,
0.561221f,  -0.158878f, -0.148091f, -0.243957f, 0.118927f,  -0.006423f,
-0.015231f, 0.137575f,  -0.187513f, -0.183042f, -0.229412f, -0.280224f,
0.311481f,  0.131624f,  0.017188f,  0.133418f,  -0.238982f, -0.014043f,
-0.033174f, 0.004408f,  0.046022f,  0.179092f,  -0.063637f, -0.338349f,
-0.233771f, -0.130741f, 0.099883f,  -0.007293f, 0.033556f,  -0.043553f,
-0.186326f, -0.030564f, -0.171473f, 0.780380f,  0.058980f,  0.789950f,
0.033544f,  -0.438068f, 0.177975f,  -0.394243f, 0.252201f,  0.000277f,
0.069758f,  -0.027393f, -0.028748f, -0.291594f, -0.300644f, 0.235721f,
-0.117545f, -0.030197f, 0.126201f,  -0.217840f, 0.133034f,  -0.049019f,
-0.019958f, -0.002331f, 0.062720f,  0.182636f,  0.087908f,  -0.408507f,
-0.325497f, 0.077945f,  0.092927f,  -0.052880f, -0.160201f, 0.130870f,
-0.314744f, 0.065331f,  -0.287756f, 0.502228f,  0.574219f,  0.465179f,
0.234652f,  -0.409270f, 0.065645f,  -0.275827f, 0.228066f,  -0.160197f,
-0.014316f, 0.089968f,  0.072272f,  -0.370058f, -0.459206f, 0.148880f,
0.207121f,  0.090773f,  -0.017553f, -0.026600f, -0.030158f, -0.343788f,
0.084305f,  0.076063f,  0.253837f,  0.281768f,  -0.089003f, -0.282088f,
-0.270604f, -0.086118f, 0.138577f,  -0.021855f, -0.070978f, 0.272630f,
-0.283237f, -0.099182f, -0.228750f, 0.203140f,  0.551886f,  0.570057f,
0.015256f,  -0.270628f, -0.076262f, -0.316633f, 0.303449f,  -0.034742f,
-0.051352f, 0.111573f,  -0.084261f, -0.309323f, -0.317615f, -0.094698f,
0.396521f,  0.271493f,  0.032813f,  0.041186f,  -0.305118f, 0.053186f,
-0.024496f, -0.069319f, 0.016187f,  -0.002766f, 0.252327f,  -0.387834f,
-0.280512f, 0.027065f,  -0.105529f, 0.152686f,  -0.028994f, -0.014187f,
-0.219148f, 0.108261f,  -0.268867f, 0.453835f,  0.103071f,  0.564238f,
0.465150f,  -0.320844f, 0.183620f,  -0.333135f, 0.053139f,  0.025184f,
0.115907f,  -0.125158f, 0.042378f,  -0.244379f, -0.296413f, 0.147231f,
-0.028292f, 0.016638f,  -0.008062f, -0.060200f, 0.029420f,  0.082850f,
-0.019618f, -0.095984f, -0.019129f, -0.152752f, 0.082748f,  -0.174354f,
-0.206752f, 0.018496f,  -0.178897f, 0.130165f,  0.062388f,  -0.096638f,
-0.449371f, 0.266300f,  -0.158123f, 0.685778f,  0.567925f,  -0.006415f,
0.408582f,  -0.229067f, 0.291954f,  -0.218927f, -0.211817f, 0.010033f,
0.224647f,  -0.210002f, -0.022498f, -0.275210f, -0.265050f, 0.234709f,
-0.082616f, -0.034882f, -0.224705f, 0.029309f,  0.194655f,  -0.401128f,
0.104200f,  0.101049f,  0.255006f,  0.449611f,  -0.184387f, -0.312581f,
-0.309154f, -0.093694f, 0.116242f,  0.013231f,  -0.101387f, 0.422146f,
-0.329292f, -0.182287f, -0.276443f, 0.244958f,  0.509967f,  0.522617f,
0.148644f,  -0.361763f, -0.026337f, -0.243617f, 0.276696f,  -0.028855f,
0.007794f,  0.094943f,  -0.137472f, -0.449815f, -0.245254f, -0.071506f,
0.367049f,  0.248885f,  0.027507f,  0.063726f,  -0.259306f, -0.047289f,
-0.000945f, -0.013730f, 0.078731f,  0.234817f,  0.017615f,  -0.372362f,
-0.302937f, -0.124482f, 0.119537f,  0.004774f,  -0.033214f, 0.273014f,
-0.418846f, 0.056658f,  -0.345161f, 0.357172f,  0.605618f,  0.565007f,
0.170632f,  -0.408176f, 0.038125f,  -0.382813f, 0.328414f,  -0.102645f,
0.029473f,  0.105506f,  -0.048647f, -0.396948f, -0.389695f, 0.042971f,
0.327669f,  0.207607f,  0.000350f,  -0.006979f, -0.173255f, -0.307395f,
-0.053452f, 0.120680f,  0.255739f,  0.332456f,  0.013426f,  -0.474096f,
-0.298916f, 0.065817f,  0.148159f,  -0.014042f, -0.223698f, 0.393038f,
-0.338369f, -0.070042f, -0.373589f, 0.504040f,  0.710039f,  0.505853f,
0.026179f,  -0.462684f, 0.064258f,  -0.348054f, 0.291485f,  -0.157772f,
-0.019152f, 0.165796f,  -0.030835f, -0.431007f, -0.506948f, 0.114943f,
0.376422f,  0.068700f,  -0.011715f, -0.006711f, -0.037347f, 0.156533f,
-0.049174f, -0.045999f, -0.080680f, -0.139524f, 0.293895f,  -0.323045f,
-0.220691f, 0.005776f,  -0.214853f, 0.161239f,  0.029343f,  -0.130737f,
-0.246302f, 0.223388f,  -0.232998f, 0.519759f,  0.167635f,  0.301192f,
0.631034f,  -0.225244f, 0.226595f,  -0.278431f, -0.124333f, 0.045793f,
0.130548f,  -0.206803f, 0.040165f,  -0.236008f, -0.231943f, 0.228075f,
-0.159354f, -0.007616f, -0.080136f, -0.061198f, 0.102430f,  -0.044000f,
-0.046244f, 0.014763f,  0.096832f,  0.165128f,  0.170414f,  -0.331759f,
-0.429112f, 0.002160f,  0.020684f,  0.068907f,  -0.093828f, 0.188599f,
-0.337311f, 0.096042f,  -0.372279f, 0.074743f,  0.409074f,  0.331038f,
0.793213f,  -0.210666f, -0.015273f, -0.226446f, 0.065123f,  -0.050365f,
0.045164f,  0.044708f,  -0.048557f, -0.182332f, -0.268392f, -0.011377f,
0.070426f,  0.056289f,  0.019044f,  0.011434f,  -0.086059f, -0.154989f,
-0.005373f, -0.083942f, 0.156126f,  0.359937f,  -0.061899f, -0.228640f,
-0.352086f, -0.079847f, 0.040400f,  0.051691f,  0.011928f,  0.167815f,
-0.372779f, 0.112271f,  -0.364243f, 0.293110f,  0.410991f,  0.361557f,
0.390498f,  -0.342884f, 0.167287f,  -0.361263f, 0.132153f,  -0.113543f,
0.170829f,  -0.134148f, 0.002776f,  -0.192569f, -0.374695f, 0.339710f,
-0.048318f, 0.060624f,  -0.006521f, -0.058608f, 0.043826f
};

APDK_END_NAMESPACE

#endif //APDK_INTERP_DATA_50_H