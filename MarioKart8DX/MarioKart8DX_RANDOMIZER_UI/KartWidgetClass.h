#ifndef KARTWIDGETCLASS_H
#define KARTWIDGETCLASS_H

#include <QWidget>
#include <QString>

class QLabel;
class QPushButton;

class KartWidgetClass : public QWidget
{
    Q_OBJECT

public:
    explicit KartWidgetClass(int playerNumber, QWidget *parent = nullptr);
    ~KartWidgetClass();

    // New function to update the combo with path
    void setPlayerCombo(const QString& characterPath, const QString& kartPath,
                        const QString& wheelsPath, const QString& gliderPath,
                       const QString& characterName, const QString& kartName,
                        const QString& wheelsName, const QString& gliderName);

signals:
    void randomizePlayerClicked(int playerNumber);

private slots:
    void onRandomizeButtonClicked();

private:
    // UI elements for images
    QLabel *m_characterImageLabel;
    QLabel *m_kartImageLabel;
    QLabel *m_wheelsImageLabel;
    QLabel *m_gliderImageLabel;

    // UI elements for names
    QLabel *m_characterNameLabel;
    QLabel *m_kartNameLabel;
    QLabel *m_wheelsNameLabel;
    QLabel *m_gliderNameLabel;

    QPushButton *m_randomizeButton;
    int m_playerNumber;
};

#endif
