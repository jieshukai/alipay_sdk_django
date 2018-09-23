class OrderInfo(models.Model):
    """订单"""

    # 订单状态：单词变大写或者小写：ctr+shift+u
    ORDER_STATUS = (
        ("PAYING", "待支付"),
        ("TRADE_SUCCESS", "支付成功"),
        ("TRADE_CLOSE", "支付关闭"),
        ("TRADE_FAIL", "支付失败"),
        ("TRADE_FINSHED", "交易结束"),
    )

    # 用户
    user = models.ForeignKey(User, verbose_name=u"用户")
    # 订单号
    # unique=True:其他数据中不能出现和当前订单一样的订单号
    order_sn = models.CharField(max_length=30, unique=True, verbose_name="订单号")
    # 交易编号，和第三方交易产生的
    trade_no = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="订单号")
    # 支付状态
    pay_status = models.CharField(default="PAYING", max_length=30, choices=ORDER_STATUS, verbose_name="订单状态")
    # 订单留言
    post_script = models.CharField(max_length=200, verbose_name="订单留言")
    # 订单金额
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    # 支付时间，什么时候支付的，这个不需要获取当前的时间
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")

    # 用户签收信息
    # 签收人
    signer_name = models.CharField(max_length=30, verbose_name="签收人")
    # 签收电话
    signer_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    # 签收地址
    address = models.CharField(max_length=200, verbose_name="收货地址")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)
