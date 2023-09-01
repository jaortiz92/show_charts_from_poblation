import matplotlib.pyplot as plt

def generate_bar_chart(
        labels, values, title, xlabel, ylabel,
        horizontal=False
    ):
    plt.style.use('seaborn')
    fig, ax = plt.subplots(1,1)
    fig.suptitle(
        title,
        fontsize='large',
        fontstyle='oblique',
        fontweight='bold'
    )
    if horizontal:
        ax.set_xlim([0, max(values) * 1.1])
        rects = ax.barh(labels, values)
    else:
        ax.set_ylim([0, max(values) * 1.1])
        rects = ax.bar(labels, values)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    format_values = ['{:,.1f}%'.format(x) for x in values]
    ax.bar_label(
        rects, padding=1, 
        labels=format_values)
    plt.show()

def generate_line_chart(
        labels, values, title, xlabel, ylabel
    ):
    plt.style.use('seaborn')
    fig, ax = plt.subplots(1,1)
    fig.suptitle(
        title,
        fontsize='large',
        fontstyle='oblique',
        fontweight='bold'
    )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(labels, values)
    plt.show()

def generate_pie_chart(labels, values, title):
    plt.style.use('seaborn')
    fig, ax = plt.subplots(1,1)
    ax.pie(values, labels=labels)
    fig.suptitle(
        title,
        fontsize='large',
        fontstyle='oblique',
        fontweight='bold'
    )
    ax.axis('equal')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    pass