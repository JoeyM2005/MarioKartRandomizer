#include <QApplication>
#include "mainwindow.h"

    int main(int argc, char *argv[])
{
    QApplication main_widget(argc, argv);
    MainWindow w;
    w.show();
    return main_widget.exec();
}
