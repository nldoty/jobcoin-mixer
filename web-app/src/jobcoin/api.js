import { MIXER_REQUEST_MIX_URL, MIXER_CHECK_DEPOSIT_URL } from '../config'

export const getUniqueMixerAddress = async (body) => {
    const url = MIXER_REQUEST_MIX_URL;

    return fetch(url,
        {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: 'POST',
            xhrFields: {
                withCredentials: true
            },
            crossDomain: true,
            body: JSON.stringify(body)
        }).then((response) => {
            return response.json();
    });
};


export const checkMixerDepositAddress = async (address) => {

    const url = `${MIXER_CHECK_DEPOSIT_URL}/${address}`;
    return fetch(url,
        {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: 'GET',
            xhrFields: {
                withCredentials: true
            },
            crossDomain: true,
        }).then((response) => {
            return response.json();
    });
};


export const mixCoinsFromAddress = async(address, body) => {
    const url = `${MIXER_CHECK_DEPOSIT_URL}/${address}`;

    return fetch(url,
        {
            body: JSON.stringify(body),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: 'POST',
            xhrFields: {
                withCredentials: true
            },
            crossDomain: true,
        }).then((response) => {
        return response.json();
    });
}