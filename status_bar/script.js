const data = [
    {
        '2023-01-01': {
            "status": 100,
            "message": "all fine"
        }
    },
    {
        "2023-01-02": {
            "status": 60,
            "message": "minor issues with webhooks"
        }
    }
];

const statusBar = document.getElementById('status-bar');

data.forEach(dayData => {
    for (const date in dayData) {
        const { status, message } = dayData[date];
        const rectangle = document.createElement('div');

        if (status === 0) {
            rectangle.className = 'rectangle status-0';
        } else if (status > 0 && status <= 40) {
            rectangle.className = 'rectangle status-40';
        } else if (status > 40 && status <= 60) {
            rectangle.className = 'rectangle status-60';
        } else if (status > 60 && status <= 80) {
            rectangle.className = 'rectangle status-80';
        } else {
            rectangle.className = 'rectangle status-100';
        }

        rectangle.setAttribute('data-message', message);
        statusBar.appendChild(rectangle);
    }
});

