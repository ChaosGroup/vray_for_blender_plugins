#!/usr/bin/python

def printChannelItems():
    channelsEnum = (
        ( True, 'REG_CHAN_VFB_ATMOSPHERE', "Atmosphere"),
        ( True, 'REG_CHAN_VFB_DIFFUSE', "Diffuse"),
        ( True, 'REG_CHAN_VFB_REFLECT', "Reflection"),
        ( True, 'REG_CHAN_VFB_REFRACT', "Refraction"),
        ( True, 'REG_CHAN_VFB_SELFILLUM', "Self Illumination"),
        ( True, 'REG_CHAN_VFB_SHADOW', "Shadow"),
        ( True, 'REG_CHAN_VFB_SPECULAR', "Specular"),
        ( True, 'REG_CHAN_VFB_LIGHTING', "Lighting"),
        ( True, 'REG_CHAN_VFB_GI', "GI"),
        ( True, 'REG_CHAN_VFB_CAUSTICS', "Caustics"),
        ( True, 'REG_CHAN_VFB_RAWGI', "Raw GI"),
        ( True, 'REG_CHAN_VFB_RAWLIGHT', "Raw Lightning"),
        ( True, 'REG_CHAN_VFB_RAWSHADOW', "Raw Shadow"),
        ( True, 'REG_CHAN_VFB_VELOCITY', "Velocity"),
        ( True, 'REG_CHAN_VFB_RENDERID', "Render ID"),
        ( True, 'REG_CHAN_VFB_MTLID', "Material ID"),
        ( True, 'REG_CHAN_VFB_NODEID', "Node ID"),
        ( True, 'REG_CHAN_VFB_ZDEPTH', "Z-Depth"),
        ( True, 'REG_CHAN_VFB_REFLECTION_FILTER', "Reflection Filter"),
        ( True, 'REG_CHAN_VFB_RAW_REFLECTION', "Raw Reflection"),
        ( True, 'REG_CHAN_VFB_REFRACTION_FILTER', "Refraction Filter"),
        ( True, 'REG_CHAN_VFB_RAW_REFRACTION', "Raw Refraction"),
        ( True, 'REG_CHAN_VFB_REALCOLOR', "Real Color"),
        ( True, 'REG_CHAN_VFB_NORMAL', "Normal"),
        ( True, 'REG_CHAN_VFB_BACKGROUND', "Background"),
        ( True, 'REG_CHAN_VFB_ALPHA', "Alpha"),
        ( True, 'REG_CHAN_VFB_COLOR', "Color"),
        ( True, 'REG_CHAN_VFB_WIRECOLOR', "Wire Color"),
        ( True, 'REG_CHAN_VFB_MATTESHADOW', "Matte / Shadow"),
        ( True, 'REG_CHAN_VFB_TOTALLIGHT', "Total Lightning"),
        ( True, 'REG_CHAN_VFB_RAWTOTALLIGHT', "Raw Total Lightning"),
        ( True, 'REG_CHAN_VFB_BUMPNORMAL', "Bump / Normal"),
        ( True, 'REG_CHAN_VFB_SAMPLERATE', "Samplerate"),
        ( True, 'REG_CHAN_VFB_SSS2', "SSS"),
        ( True, 'REG_CHAN_DRBUCKET', "DR Bucket"),
        ( True, 'REG_CHAN_VFB_VRMTLREFLECTGLOSS', "Reflection Glossiness"),
        ( True, 'REG_CHAN_VFB_VRMTLREFLECTHIGLOSS', "Reflection Hilights"),
        ( True, 'REG_CHAN_VFB_VRMTLREFRACTGLOSS', "Refraction Glossiness"),
        ( True, 'REG_CHAN_VFB_SHADEMAP_EXPORT', "Shademap Export"),
        ( True, 'REG_CHAN_VFB_REFLECT_ALPHA', "Reflection Alpha"),
        ( True, 'REG_CHAN_VFB_VRMTLREFLECTIOR', "Reflection IOR"),
        ( True, 'REG_CHAN_VFB_MTLRENDERID', "Material Render ID"),
        ( True, 'REG_CHAN_VFB_NOISE_LEVEL', "Noise Level"),
    )

    for i,channelEnum in enumerate(channelsEnum):
        if channelsEnum[0]:
            print('[ "%i", "%s", "" ]%s' % (i+100, channelEnum[2], ',' if i < len(channelsEnum) - 1 else ''))


if __name__ == '__main__':
    printChannelItems()
