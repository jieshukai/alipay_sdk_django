def alipay_return(request):
    process_query = {}
    if request.method == 'POST':
        process_query = {k: v for k, v in request.POST.items()}
    if request.method == 'GET':
        process_query = {k: v for k, v in request.GET.items()}
    ali_sign = process_query.pop('sign', None)
    alipay = AliPay(
        appid=ALIPAY_APPID,
        app_notify_url=RETURN_URL,
        app_private_key_path=APP_PRIVATE_KEY,
        alipay_public_key_path=ALIPAY_PUBLIC_KEY,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=ALIPAY_DEBUG,  # 默认False,
        return_url=RETURN_URL
    )
    check_result = alipay.verify(process_query, ali_sign)
    if check_result:
        order_sn = process_query.get('out_trade_no', None)
        trade_no = process_query.get('trade_no', None)
        orderinfos = OrderInfo.objects.filter(order_sn=order_sn)
        for orderinfo in orderinfos:
            # 得到订单里所有的商品
            ordergoods = orderinfo.goods.all()
            for ogoods in ordergoods:
                goods = ogoods.goods
                goods.sold_num += ogoods.goods_num
                goods.save()

            orderinfo.trade_no = trade_no
            orderinfo.pay_status = 'TRADE_SUCCESS'
            orderinfo.pay_time = datetime.now()
            orderinfo.save()
            print('ali--success')
        response = redirect(reverse('index'))
        response.set_cookie('nextPath', 'pay', max_age=2)
        return response
    print('ali---fail')
    return redirect(reverse('index'))
