function bridgeCrossing(n, w, l, trucks) {
    const queue = [...trucks];
    const bridge = Array(w).fill(0);
    let time = 0;
    let bridgeSum = 0;

    while (queue.length > 0) {
        time++;
        bridgeSum -= bridge.shift()

        const nextTrue = queue[0]
        if (bridgeSum + nextTrue <= 1) {
            bridgeSum += nextTrue;
            bridge.push(queue.shift());
        } else {
            bridge.push(0);
        }
    }

    return time + w;
}
