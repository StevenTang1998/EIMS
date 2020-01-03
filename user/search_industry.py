from pyecharts.charts import Geo, Pie, Bar
from pyecharts import options as opts


def industry_distribute(industry_count, province):
    c = (
        Pie(init_opts=opts.InitOpts(height='750px', width='100%',
                                    animation_opts=opts.AnimationOpts(animation_delay=100,
                                                                      animation_easing="elasticOut")))
            .add(
            "",
            industry_count,
            center=["40%", "50%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title=("全中国" if province == "不限" else province) + "行业分布图",
                                      pos_left='center',
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_left="80%", orient="vertical"
            ),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    lines = c.render_embed().split('\n')
    return lines[9], '\n'.join(lines[10:-3])


def province_distribute(province_count, industry):
    data = []
    for (p, c) in province_count:
        if len(p) in range(2, 9):
            data.append((p[:2] if p[0] not in ['内', '黑'] else p[:3], c))

    c = (
        Geo(init_opts=opts.InitOpts(height='750px', width='100%',
                                    animation_opts=opts.AnimationOpts(animation_delay=100,
                                                                      animation_easing="elasticOut")))
            .add_schema(maptype="china")
            .add("", data, symbol_size=20)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=max([c for (p, c) in data])),
            title_opts=opts.TitleOpts(title="全中国" + ("" if industry == "不限" else industry) + "企业数量分布图",
                                      subtitle="每个点的数字代表该省企业的数量", pos_left='center',
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=30),
                                      subtitle_textstyle_opts=opts.TextStyleOpts(font_size=15)),
        )
    )
    lines = c.render_embed().split('\n')
    return lines[10], '\n'.join(lines[11:-3])


def draw_capital(Y, province, industry):
    X = []
    for i in range(1, 50):
        X.append(str(i * 10) + '万元～' + str((i + 1) * 10) + '万元')
    X.append('500万元以上')
    count = [0] * 50
    for (i, ) in Y:
        count[min(50, i // 10) - 1] += 1
    X.reverse()
    count.reverse()

    c = (
        Bar(init_opts=opts.InitOpts(height='750px', width='100%',
                                    animation_opts=opts.AnimationOpts(animation_delay=100,
                                                                      animation_easing="elasticOut")))
            .add_xaxis(X)
            .add_yaxis("", count)
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(
            title_opts=opts.TitleOpts(title=("全中国" if province == "不限" else province) + industry + "注册资本图",
                                      subtitle="每个柱的数字代表该注册资本范围内企业的数量", pos_left='center',
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=30),
                                      subtitle_textstyle_opts=opts.TextStyleOpts(font_size=15)),
            xaxis_opts=opts.AxisOpts(is_show=False), yaxis_opts=opts.AxisOpts(boundary_gap=['200', '200']),
            datazoom_opts=opts.DataZoomOpts(orient="vertical"))
    )
    lines = c.render_embed().split('\n')
    return lines[9], '\n'.join(lines[10:-3])
