#include "kartwidgetclass.h"
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QPixmap>

KartWidgetClass::KartWidgetClass(int playerNumber, QWidget *parent){
    // : QWidget{parent}, m_playerNumber(playerNumber);

    // Initialize image and name labels
    m_characterImageLabel = new QLabel();
    m_characterNameLabel = new QLabel("Character: N/A");
    m_kartImageLabel = new QLabel();
    m_kartNameLabel = new QLabel("Kart: N/A");
    // ... repeat for wheels and glider

    m_randomizeButton = new QPushButton("Randomize This Player");

    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->addWidget(new QLabel(QString("Player %1").arg(playerNumber)));

    // Add layouts for each component to hold image and name
    QHBoxLayout *characterLayout = new QHBoxLayout();
    characterLayout->addWidget(m_characterImageLabel);
    characterLayout->addWidget(m_characterNameLabel);
    mainLayout->addLayout(characterLayout);

    // ... repeat for kart, wheels, and glider layouts

    mainLayout->addWidget(m_randomizeButton);
    connect(m_randomizeButton, &QPushButton::clicked, this, &KartWidgetClass::onRandomizeButtonClicked);
}

void KartWidgetClass::setPlayerCombo(const QString& characterPath, const QString& kartPath,
                                     const QString& wheelsPath, const QString& gliderPath,
                                     const QString& characterName, const QString& kartName,
                                     const QString& wheelsName, const QString& gliderName)
{
    // Load and scale the images. You might want to define a fixed size.
    QPixmap characterPixmap(characterPath);
    m_characterImageLabel->setPixmap(characterPixmap.scaled(64, 64, Qt::KeepAspectRatio));
    m_characterNameLabel->setText(characterName);

    // ... repeat for kart, wheels, and glider
}
