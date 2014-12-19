## Support JPEG

在ubuntu 使用pillow 库处理jpg 图片的时候出现问题：

    OError: broken data stream when reading image file

最后通过源码安装libjpeg8 搞定：[参考这里](http://askubuntu.com/questions/211627/how-to-add-support-for-the-jpeg-image-format)

Google 了半天，先后参考了:

http://askubuntu.com/questions/211627/how-to-add-support-for-the-jpeg-image-format

http://stackoverflow.com/questions/8915296/python-image-library-fails-with-message-decoder-jpeg-not-available-pil

http://stackoverflow.com/questions/7877330/django-os-x-wrong-jpeg-library-version-library-is-80-caller-expects-62-sorl-th

http://stackoverflow.com/questions/24815508/python-django-mezzanine-install-fail-for-pillow-package

http://stackoverflow.com/questions/10099391/python-2-7-pil-open-the-picture-of-jpeg-format-error-mac-lion

http://stackoverflow.com/questions/7652249/how-to-solve-ioerrorbroken-data-stream-when-reading-image-file

不过安装pillow 过程的这个警告依然没解决:

    warning: no files found matching '*.bdf' under directory 'Images'

先不管它了。

注： pillow 是PIL 的替代品，PIL 貌似没人更新了，现在一般都用pillow 处理图片。

