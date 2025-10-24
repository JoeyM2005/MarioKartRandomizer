#include "mainwindow.h"
#include "kartwidgetclass.h"
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QSpinBox>
#include <QPushButton>
#include <QLabel>
#include <QWidget>

    MainWindow::MainWindow(QWidget *parent)
    : QMainWindow{parent}
{
    setupUI();
}

MainWindow::~MainWindow()
{
    // Child widgets will be automatically deleted by their parent.
}

void MainWindow::setupUI()
{
    // Central widget to hold all layouts
    QWidget *centralWidget = new QWidget(this);
    setCentralWidget(centralWidget);

    QVBoxLayout *mainLayout = new QVBoxLayout(centralWidget);
    QHBoxLayout *controlsLayout = new QHBoxLayout();

    // Player count controls
    QLabel* playerCountLabel = new QLabel("Number of Players:");
    m_playerCountSpinBox = new QSpinBox();
    m_playerCountSpinBox->setRange(1, 4);
    m_playerCountSpinBox->setValue(2); // Default to 2 players

    // Buttons
    m_randomizeAllButton = new QPushButton("Randomize All");

    controlsLayout->addWidget(playerCountLabel);
    controlsLayout->addWidget(m_playerCountSpinBox);
    controlsLayout->addWidget(m_randomizeAllButton);
    mainLayout->addLayout(controlsLayout);

    // Connect player count spinbox to update the UI
    connect(m_playerCountSpinBox, qOverload<int>(&QSpinBox::valueChanged), this, &MainWindow::onNumberOfPlayersChanged);

    // Initial setup for 2 players
    updatePlayerWidgets(m_playerCountSpinBox->value());
}

void MainWindow::updatePlayerWidgets(int playerCount)
{
    // First, clear any existing widgets
    for (KartWidgetClass* widget : m_playerWidgets) {
        widget->hide();
        // Qt's parent-child relationship handles memory management
    }
    m_playerWidgets.clear();

    // Now, create the new widgets
    QHBoxLayout* playersLayout = new QHBoxLayout();
    for (int i = 0; i < playerCount; ++i) {
        KartWidgetClass* playerWidget = new KartWidgetClass(i + 1, this);
        playersLayout->addWidget(playerWidget);
        m_playerWidgets.append(playerWidget);
        // Connect each player's randomize button to a slot in the main window
        connect(playerWidget, &KartWidgetClass::randomizePlayerClicked, this, &MainWindow::onRandomizeSpecificPlayer);
    }

    // Find the main layout and add the new player layout
    if (auto* mainLayout = qobject_cast<QVBoxLayout*>(centralWidget()->layout())) {
        mainLayout->addLayout(playersLayout);
    }

    // Connect the master randomize button
    connect(m_randomizeAllButton, &QPushButton::clicked, this, &MainWindow::onRandomizeAllClicked);
}

void MainWindow::onRandomizeAllClicked()
{
    // This is where you will call your C++ randomizer logic for all players
    // and then update each widget in m_playerWidgets with the new data.
    // E.g., for(int i=0; i<m_playerWidgets.size(); ++i) {
    //      // Call your randomizer for player i+1
    //      // m_playerWidgets[i]->setPlayerCombo(...);
    // }
}

void MainWindow::onRandomizeSpecificPlayer(int playerNumber)
{
    // This is where you'll call your C++ randomizer logic for a single player
    // and then update that specific player's widget.
    // E.g., m_playerWidgets[playerNumber - 1]->setPlayerCombo(...);
}

void MainWindow::onNumberOfPlayersChanged(int count)
{
    // When the user changes the number of players, regenerate the UI
    updatePlayerWidgets(count);
}
