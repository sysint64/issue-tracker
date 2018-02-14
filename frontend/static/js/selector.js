function addEventListenerForQuery(items, eventName, listener) {
    for (let i = 0; i < items.length; i++)
        items[i].addEventListener(eventName, listener);
}
