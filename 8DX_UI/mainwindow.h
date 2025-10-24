#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QList>

class KartWidgetClass;
class QSpinBox;
class QPushButton;
class QHBoxLayout; // Add this

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void onRandomizeAllClicked();
    void onRandomizeSpecificPlayer(int playerNumber);
    void onNumberOfPlayersChanged(int count);

private:
    void setupUI();
    void updatePlayerWidgets(int playerCount);

    // Add these member variables
    QList<KartWidgetClass*> m_playerWidgets;
    QSpinBox* m_playerCountSpinBox;
    QPushButton* m_randomizeAllButton;
    QHBoxLayout* m_playersLayout; // Add this
};

#endif
