function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function setSessionValue(key, value, callback) {
    fetch("/set-sessions/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
            session_key: key,
            session_value: value
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log("Session Set:", data);
            if (callback) callback();
        });
}



function getSessionValue(key) {
    return fetch(`/set-sessions/?session_key=${key}`)
        .then(response => response.json())
        .then(data => {
            console.log("Session Value:", data.session);
            return data.session;
        });
}

function checkCompanySelect() {
    getSessionValue('selected_company').then(function (value) {
        if (value === null || value === "null" || value === "" || value === 0) {
            const modal = document.getElementById('crypto-modal');
            if (modal !== null) {
                const modalInstance = new Modal(modal);
                modalInstance.show();
            }
        }
    });
}



function selectCompany(id) {
    setSessionValue('selected_company', id, () => {
        const modalEl = document.getElementById('crypto-modal');
        if (modalEl) {
            const modalInstance = new Modal(modalEl, {
                placement: 'center',
                backdrop: 'dynamic',
                backdropClasses: 'bg-gray-900 bg-opacity-50 fixed inset-0 z-40',
                closable: true,
            });
            modalInstance.hide();
            setSessionValue('selected_branch', 0);
            location.reload();
        }
    });
}


function filterByBranch(branchName) {
    setSessionValue('selected_branch', branchName, () => {
        location.reload();
    });
}

