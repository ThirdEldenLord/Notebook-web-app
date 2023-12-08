function deleteNote(noteId) {
    fetch('/delete-note',{
        method: 'POST',
        bode: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = "/notes"
    });
}